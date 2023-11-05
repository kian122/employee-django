from django.contrib import admin

# importing model
from .models import EmployeeModel

# Register your models here.

admin.site.register(EmployeeModel)