from django.urls import path 

# the import for views
from . import views

urlpatterns = [
    path('', views.frontpage),
]