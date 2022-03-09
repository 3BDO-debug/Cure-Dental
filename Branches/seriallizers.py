from rest_framework.serializers import ModelSerializer
from . import models

class BranchesSerializer(ModelSerializer):
    class Meta:
        model = models.Branch
        fields = '__all__'