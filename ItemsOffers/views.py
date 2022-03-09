from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers

# Create your views here.
@api_view(["GET"])
def items_offers_handler(request):
    items_offers = models.ItemOffer.objects.all()
    serializer = serializers.ItemsOffersSeriallizer(items_offers, many=True)

    return Response(serializer.data)