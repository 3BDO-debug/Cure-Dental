from django.db import models

# Create your models here.
class Case(models.Model):
    case_img = models.ImageField()
    patient_name = models.CharField(max_length=350, verbose_name="Case Name")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Case"
        verbose_name_plural = "Cases"

    def __str__(self):
        return self.patient_name