from rest_framework.serializers import ModelSerializer
from . import models

class ConsultationSerializer(ModelSerializer):
    class Meta:
        model = models.Consultation
        fields = ('name', 'phone', 'msg')