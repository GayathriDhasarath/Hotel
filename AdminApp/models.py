from django.db import models

# Create your models here.
class Viewtable(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField(max_length=80)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images',default='null.jpg')
    def __str__(self):
        return self.name

class Travel_mod(models.Model):
    dest=models.CharField(max_length=50)
    desc=models.TextField(max_length=80)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images',default='null.jpg')
    def __str__(self):
        return self.dest
