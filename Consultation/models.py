from django.db import models

# Create your models here.
class Consultation(models.Model):
    name = models.CharField(max_length=500, verbose_name="Name") 
    phone = models.CharField(max_length=500, verbose_name="Phone Number") 
    msg = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Consultation"
        verbose_name_plural = "Consultations"

    def __str__(self):
        return self.name