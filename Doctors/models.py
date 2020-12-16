from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_photo = models.ImageField()
    doctor_name = models.CharField(max_length=500, verbose_name="Doctor's Name")
    speciality = models.CharField(max_length=750, verbose_name="Doctor's Speciality")

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
    
    def __str__(self):
        return self.doctor_name
    