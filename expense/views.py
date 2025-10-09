from django.shortcuts import render
from .serializers import ExpenseSerializer, CategorySerialzer
from rest_framework import viewsets
from .models import Expense, Category
from rest_framework.permissions import IsAuthenticated

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all() #to reafetch all expenses from the database
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated] #only authenticated users can access this viewset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer
    permission_classes = [IsAuthenticated]

# Create your views here.
