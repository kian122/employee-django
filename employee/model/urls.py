from django.urls import path 

# the import for views
from . import views


# log func import
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.frontpage , name="frontpage"),
    path('login/' , auth_views.LoginView.as_view(template_name = "model/login.html") , name="login"),
    path('create/', views.create, name="create"),
    path('view/', views.view , name="view"),
    path('detail/<str:pk>', views.detail , name="detail"),
    path('remove/<str:pk>', views.remove , name="remove"),
    path('edit/<str:pk>' , views.edit , name="edit")
]
