from django.db import models

# Create your models here.

# employee field
class Employee(models.Model):
    name = models.CharField( max_length=100)
    last_name = models.CharField( max_length=100)
    phone_number = models.IntegerField( max_length=20 , unique=True)
    email = models.EmailField( max_length=255 , unique=True)
    started_at = models.TimeField( auto_now=True)

    def __str__(self):
        return  str(self.name)  + " - " + str(self.phone_number)