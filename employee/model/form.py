from . import models

from django import forms

# employee class
class EmployeeClass (forms.Form):
    class Meta:
        model = models.employee
        fields = "__all__"