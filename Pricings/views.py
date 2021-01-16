from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers
# Create your views here.
@api_view(['GET'])
def pricings_handler(request):
    pricings = models.Pricing.objects.all()
    serializer = serializers.PricingSerializer(pricings, many=True)
    return Response(serializer.data)
