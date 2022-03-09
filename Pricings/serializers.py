from rest_framework import serializers
from . import models

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pricing
        fields = '__all__'