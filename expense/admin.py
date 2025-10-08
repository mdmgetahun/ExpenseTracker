from django.contrib import admin
from .models import CustomUser, Expense, Category

admin.site.register(CustomUser)
admin.site.register(Expense)
admin.site.register(Category)

# Register your models here.
