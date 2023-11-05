from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.http import HttpResponseNotFound

# importing forms
from .form import EmployeeForm

# importing models
from .models import EmployeeModel

# Create your views here.

""""""

# front page view def
def frontpage( request):
    return render( request , "model/frontpage.html")

# log in
def log( request):
    return render( request , "model/login.html")

def detail( request , pk):
    try:
        model = EmployeeModel.objects.get( id = pk)
    except:
        return HttpResponseNotFound()
    return render( request , "model/detail.html" , {"model":model})

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

def view( request):
    #defining]
    model = EmployeeModel.objects.all()

    return render( request , "model/view.html" , {"model":model})