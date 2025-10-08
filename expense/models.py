from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    currency = models.CharField(max_length=3, default='EUR')

    def __str__(self):
        return self.username
    
class Expense(models.Model):
    user = models.ForeignKey(
        
        settings.AUTH_USER_MODEL, related_name='expenses', 
        on_delete=models.SET_NULL, null=True, blank=True
        )
    category = models.ForeignKey('Category', related_name='expenses', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} on {self.date}"

    
class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Create your models here.
