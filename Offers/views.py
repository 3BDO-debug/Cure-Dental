from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models,serializers
# Create your views here.
@api_view(['GET'])
def offers_handler(request):
    offers = models.Offer.objects.all()[0:1]
    serializer = serializers.OfferSerializer(offers, many=True)
    return Response(serializer.data)