from django.db import models

# Create your models here.
class Contact_details(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    sub=models.CharField(max_length=80)
    message=models.TextField(max_length=250)
    def __str__(self):
       return self.name
class User_details(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    contact=models.IntegerField()
    password=models.CharField(max_length=15)
    confirm_password=models.CharField(max_length=15)
    def __str__(self):
        return self.name
