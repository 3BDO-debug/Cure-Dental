from rest_framework.serializers import ModelSerializer
from . import models

class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = ('name','phone','msg')