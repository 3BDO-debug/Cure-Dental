from rest_framework.serializers import ModelSerializer
from . import models

class BookingSerializer(ModelSerializer):
    class Meta:
        model = models.Booking
        fields = (
            'name',
            'age',
            'date_of_birth',
            'phone_number',
            'email',
            'address',
            'branch',
            
        )