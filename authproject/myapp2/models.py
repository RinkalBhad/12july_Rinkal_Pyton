from django.db import models

# Create your models here.

class emp(models.Model):
    name=models.CharField(max_length=10)
    city=models.CharField(max_length=10)


class peoplesign(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    city=models.CharField(max_length=10)
    state=models.CharField(max_length=10)
    number=models.BigIntegerField()

    class Meta:
        db_table="peoplesign"