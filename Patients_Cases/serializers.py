from rest_framework.serializers import ModelSerializer
from . import models

class CasesSeriallizer(ModelSerializer):
    class Meta:
        model = models.Case
        fields = ('case_img', 'patient_name',)
        