from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_photo = models.ImageField()
    doctor_english_name = models.CharField(max_length=500, verbose_name="Doctor's English Name")
    doctor_arabic_name = models.CharField(max_length=500, verbose_name="Doctor's Arabic Name")
    speciality_in_english = models.CharField(max_length=750, verbose_name="Doctor's Speciality in english")
    speciality_in_arabic = models.CharField(max_length=750, verbose_name="Doctor's Speciality in arabic")

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return self.doctor_english_name
