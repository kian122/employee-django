from .models import EmployeeModel

from django import forms

# employee class
class EmployeeForm (forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"