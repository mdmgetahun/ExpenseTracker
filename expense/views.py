from django.shortcuts import render
from .serializers import ExpenseSerializer, CategorySerializer, RegisterSerializer
from rest_framework import viewsets, status
from .models import Expense, Category
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate    
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
from .models import Expense
from django.db.models import Sum

class RegisterAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=201) #status 201 indicates successful creation
        return Response({"errors": serializer.errors,
                         "message": "check input data"}, status=400) #this will return any validation errors if the data is not valid

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
      
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
        else:
            return Response({"error": "Invalid credentials"}, status=401)

class ExpenseViewSet(viewsets.ModelViewSet):

    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated] #only allows authenticated users to  access this viewset
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'date'] #enables filtering by category and date


    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user) #makes sure that users can only see their own expenses

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
class MonthlyExpenseAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, year, month):
        user=request.user   # Get the authenticated user
        expenses=Expense.objects.filter(user=user, date__year=year, date__month=month) 
        grand_total= expenses.aggregate(total=Sum('amount'))['total'] or 0 # Calculate the grand total of expenses for the month  
        per_category = expenses.values('category__name').annotate(total=Sum('amount')) # Calculate total expenses per category
        serializer=ExpenseSerializer(expenses, many=True)
        return Response({"expenses": serializer.data, "grand_total": grand_total, "per_category": list(per_category)})

# Create your views here.
