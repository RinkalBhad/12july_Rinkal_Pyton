from django.db import models

# Create your models here.
class usersignup(models.Model):
    
    fistname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    city=models.CharField(max_length=10)
    state=models.CharField(max_length=10)
    number=models.BigIntegerField()




