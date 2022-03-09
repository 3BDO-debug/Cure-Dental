from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from . import models
from . import serializers

# Create your views here.
@api_view(["GET"])
def cases_view(request):
    cases = models.Case.objects.all()
    serializer = serializers.CasesSeriallizer(cases, many=True)

    return Response(serializer.data)