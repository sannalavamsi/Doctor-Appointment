from rest_framework import serializers
from . import models

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = ('id', 'doctor_name','speciality')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ('id', 'doctor','patient_name','registered_date','waiting_status')
