from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers,models
# Create your views here.
@api_view(['POST'])
def booking_handler(request):
    seriallizer = serializers.BookingSerializer(models.Booking(), data=request.data)
    if seriallizer.is_valid():
        seriallizer.save()
        return Response(seriallizer.data, status=status.HTTP_201_CREATED)
    return Response(seriallizer.errors, status=status.HTTP_400_BAD_REQUEST)