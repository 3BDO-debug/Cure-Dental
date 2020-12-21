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
    api_response = []
    for data in cases:
        response = {
            "source": {"uri": f"https://cure-dental.herokuapp.com/media/{data.case_before_img.name}"},
            "source2":{"uri": f"https://cure-dental.herokuapp.com/media/{data.case_after_img.name}"},
            'width':806,
            'height':720,
        }
        api_response.append(response)
    return JsonResponse(api_response, safe=False)