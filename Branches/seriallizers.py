from rest_framework.serializers import ModelSerializer
from . import models

class BranchesSerializer(ModelSerializer):
    class Meta:
        model = models.Branch
        fields = ('branc_img','branch_name','branch_address','branch_phone','branch_manager')