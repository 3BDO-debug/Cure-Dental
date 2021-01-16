from rest_framework import serializers
from . import models

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pricing
        fields = ('item_name', 'item_price')