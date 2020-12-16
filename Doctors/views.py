from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers
# Create your views here.
@api_view(['GET'])
def doctors_view(request):
    doctors = models.Doctor.objects.all()
    seriallizer = serializers.DoctorSeriallizer(doctors, many=True)
    return Response(seriallizer.data)