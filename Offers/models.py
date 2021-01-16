from django.db import models

# Create your models here.
class Offer(models.Model):
    offer_english_text = models.TextField(verbose_name="Offer's English Text")
    offer_arabic_text = models.TextField(verbose_name="Offer's Arabic Text")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"

    def __str__(self):
        return self.offer