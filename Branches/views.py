from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import seriallizers
from . import models
# Create your views here.
@api_view(['GET'])
def branches_view(request):
    branches = models.Branch.objects.all()
    serializer = seriallizers.BranchesSerializer(branches, many=True)
    return Response(serializer.data)