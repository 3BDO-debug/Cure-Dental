from rest_framework import serializers
from . import models


class DoctorSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = ("doctor_photo", "doctor_name", "speciality")
