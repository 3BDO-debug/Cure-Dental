from django.db import models

# Create your models here.
class Branch(models.Model):
    branch_img = models.ImageField()
    branch_name = models.CharField(max_length=350, verbose_name="Branch Name")
    branch_address = models.CharField(max_length=500, verbose_name="Branch Address")
    branch_phone = models.CharField(max_length=500, verbose_name="Branch Phone")
    branch_manager = models.CharField(max_length=50, verbose_name="Branch Manager")
    
    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.branch_name