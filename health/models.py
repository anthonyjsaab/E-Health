from django import forms
from django.db import models


# Create your models here.


class ClientInfo(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    confirmation = models.CharField(max_length=32)
    conditions = models.CharField(max_length=500)
    birth = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()


class DoctorInfo(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    confirmation = models.CharField(max_length=32)
    emailDr = models.CharField(max_length=60)
    specialization = models.CharField(max_length=500)
    hospital = models.CharField(max_length=100)


class ConfirmedAppointment(models.Model):
    time = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    drname = models.CharField(max_length=100)
    description = models.TextField()
