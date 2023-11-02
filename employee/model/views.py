from django.shortcuts import render

# importing forms
from .form import EmployeeForm

# Create your views here.

""""""

# front page view def
def frontpage( request):
    return render( request , "model/frontpage.html")

# log in
def log( request):
    return render( request , "model/login.html")

# create employee
def create( request):
    return render( request , "model/create.html")