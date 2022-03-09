from rest_framework.serializers import ModelSerializer
from . import models


class TipSerializer(ModelSerializer):
    class Meta:
        model = models.Tip
        fields = '__all__'