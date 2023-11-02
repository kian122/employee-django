from .models import Employee

from django import forms

# employee class
class EmployeeForm (forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"