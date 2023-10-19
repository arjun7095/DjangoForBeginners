from django.db import models
from pyexpat import model
class students(models.Model):
    GENDER_CHOICES=[
        ('M','MALE'),
        ('F','FEMALE')
        ]
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    emailid=models.EmailField(max_length=50)
    mobno=models.CharField(max_length=10)
    gender=models.CharField(choices= GENDER_CHOICES,max_length=1)
    address=models.TextField(max_length=1000)
    dept_name=models.ManyToManyField('departments')
    dob=models.DateField()
class departments(models.Model):
    dept_name=models.CharField(max_length=20)
class locations(models.Model):
    location=models.CharField(max_length=100)

