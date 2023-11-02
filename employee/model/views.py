from django.shortcuts import render

# Create your views here.

def frontpage( request):
    return render( request , "model/frontpage.html")

# log in
def log( request):
    return render( request , "model/login.html")

# create employee
def create( request):
    return render( request , "model/create.html")