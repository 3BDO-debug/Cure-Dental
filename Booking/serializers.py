from rest_framework.serializers import ModelSerializer
from . import models

class BookingSerializer(ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'