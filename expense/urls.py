from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, CategoryViewSet, RegisterAPIView, LoginAPIView, MonthlyExpenseAPIView

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('monthly-expense/<int:year>/<int:month>/', MonthlyExpenseAPIView.as_view(), name='monthly-expenses')
    
]