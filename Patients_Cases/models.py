from django.db import models

# Create your models here.
class Case(models.Model):
    case_before_img = models.ImageField(default='before.jpg',verbose_name="Patient Case Before Image")
    case_after_img = models.ImageField(default='after.jpg',verbose_name="Patient Case After Image")
    patient_english_name = models.CharField(max_length=350, verbose_name="Case's English Name")
    patient_arabic_name = models.CharField(max_length=350, verbose_name="Case's Arabic Name")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Case"
        verbose_name_plural = "Cases"

    def __str__(self):
        return self.patient_name