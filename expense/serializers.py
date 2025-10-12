from rest_framework import serializers
from .models import Expense, CustomUser, Category
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # user.set_password(validated_data['password'])
        # user.save()
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

    def create(self, validated_data):
        user = self.context['request'].user #makes sure every category is linked to the logged in user
        return Category.objects.create(user=user, **validated_data)

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'category', 'amount', 'description', 'date')

    def create(self, validated_data):
        user = self.context['request'].user #makes sure every expense is linked to the logged in user
        return Expense.objects.create(user=user, **validated_data)
        

