
from pyexpat import model
from django.db import models

# Create your models here.
class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False, null=False)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.speciality

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False, null=False)
    gender = models.CharField(max_length=100,blank=False, null=False)
    age= models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name



class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True)
    waiting_status = models.BooleanField(default=True)

    