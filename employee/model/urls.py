from django.urls import path 

# the import for views
from . import views

urlpatterns = [
    path('', views.frontpage),
    path('Log_In/', views.frontpage),
    path('create_employee/', views.frontpage),
]
