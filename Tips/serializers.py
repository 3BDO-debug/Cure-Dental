from rest_framework.serializers import ModelSerializer
from . import models


class TipSerializer(ModelSerializer):
    class Meta:
        model = models.Tip
        fields = ("tip_image", "tip_english_text", "tip_arabic_text")
