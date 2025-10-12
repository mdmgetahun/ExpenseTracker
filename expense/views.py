from django.shortcuts import render
from .serializers import ExpenseSerializer, CategorySerializer, RegisterSerializer
from rest_framework import viewsets, status
from .models import Expense, Category
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate    
from rest_framework.authtoken.models import Token

class RegisterAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=201) #status 201 indicates successful creation
        return Response(serializer.errors, status=400) #this will return any validation errors if the data is not valid

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
    queryset = Expense.objects.all() #to fetch all expenses from the database
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated] #only allows authenticated users to  access this viewset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]




# Create your views here.
 