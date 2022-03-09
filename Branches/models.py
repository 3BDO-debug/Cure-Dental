from django.db import models

# Create your models here.
class Branch(models.Model):
    branch_img = models.ImageField()
    branch_english_name = models.CharField(
        max_length=350, verbose_name="Branch English Name"
    )
    branch_arabic_name = models.CharField(
        max_length=350, verbose_name="Branch Arabic Name"
    )
    branch_english_address = models.CharField(
        max_length=500, verbose_name="Branch English Address"
    )
    branch_arabic_address = models.CharField(
        max_length=500, verbose_name="Branch Arabic Address"
    )

    branch_google_maps_address = models.CharField(
        max_length=750, verbose_name="Google Maps Location"
    )
    branch_phone_english_number = models.CharField(
        max_length=500, verbose_name="Branch Phone's English Number"
    )
    branch_phone_arabic_number = models.CharField(
        max_length=500, verbose_name="Branch Phone's Arabic Number"
    )

    branch_manager_english_name = models.CharField(
        max_length=50, verbose_name="Branch Manager's English Name"
    )
    branch_manager_arabic_name = models.CharField(
        max_length=50, verbose_name="Branch Manager's Arabic Name"
    )

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.branch_english_name