from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=350, verbose_name="First Name")
    age = models.CharField(max_length=350, verbose_name="Age")
    date_of_birth = models.CharField(max_length=350, verbose_name="Date Of Birth")
    phone_number = models.CharField(max_length=350, verbose_name="Phone Number")
    email = models.CharField(max_length=350, verbose_name="Email Address")
    address = models.CharField(max_length=350, verbose_name="Address")
    branch = models.CharField(max_length=350, verbose_name="Choosed Branch")
    boooked_at = models.DateTimeField(verbose_name="Booked At", auto_now_add=True)
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"New Booking By {self.name}"