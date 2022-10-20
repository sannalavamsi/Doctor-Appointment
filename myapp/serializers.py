from rest_framework import serializers
from . import models

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = ['name','speciality']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ['name','gender','age']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = ['doctor','patient','date','waiting_status']

        