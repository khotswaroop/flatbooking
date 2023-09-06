from django.db import models
from datetime import date

# Create your models here.

class Registration(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    date=models.DateField()

class FlatBooking(models.Model):
    City=models.CharField(max_length=20)
    ResidencyName=models.CharField(max_length=20)
    FlatNomber=models.IntegerField()
    FlowrNomber=models.IntegerField()
    Date=models.DateField(blank=True,null=True)

class AddContact(models.Model):
    city=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    email=models.EmailField()

class AddContactUs(models.Model):
    name=models.CharField(max_length=20)
    contactus=models.CharField(max_length=20)
    email=models.EmailField()
