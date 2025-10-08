from rest_framework import serializers
from rest_framework.routers import DefaultRouter
from .models import Expense, CustomUser, Category


class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = {'id', 'name'}

    def create(self, validated_data):
        user = self.context['request'].user #makes sure every category is linked to the logged in user
        return Category.objects.create(user=user, **validated_data)

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = {'id', 'username'}

    def create