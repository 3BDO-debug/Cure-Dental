from rest_framework import serializers
from . import models


class DoctorSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = '__all__'