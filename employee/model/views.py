from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect

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
@login_required
def create( request):
    # define
    form = EmployeeForm

    # logic
    if request.method == "POST":
        form = form( request.POST)
        if form.is_valid():
            form.save()
            return redirect("frontpage")

    return render( request , "model/create.html" , {"form":form})