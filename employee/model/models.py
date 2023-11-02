from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField( max_length=100)
    last_name = models.CharField( max_length=100)
    phone_number = models.IntegerField( max_length=20)
    email = models.EmailField( max_length=255)
    started_at = models.TimeField( auto_now=True)