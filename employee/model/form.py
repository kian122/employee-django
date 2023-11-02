from . import models

from django import forms

# employee class
class EmployeeForm (forms.Form):
    class Meta:
        model = models.employee
        fields = "__all__"