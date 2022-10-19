
from django.db import models

# Create your models here.
class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.speciality

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    registered_date= models.DateTimeField(auto_now_add=True)
    waiting_status = models.BooleanField(default=True)

    def __str__(self):
        return self.patient_name



    
    