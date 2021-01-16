from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers, models
# Create your views here.
@api_view(['GET'])
def tip_view(request):
    tips = models.Tip.objects.all().order_by("-created_at")[0:1]
    serializer = serializers.TipSerializer(tips, many=True)
    return Response(serializer.data)