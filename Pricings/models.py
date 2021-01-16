from django.db import models

# Create your models here.
class Pricing(models.Model):
    item_english_name = models.CharField(max_length=350, verbose_name="Item's English Name")
    item_arabic_name = models.CharField(max_length=350, verbose_name="Item's Arabic Name")

    item_price = models.FloatField(verbose_name="Item Price")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Pricing"
        verbose_name_plural = "Pricings"
    def __str__(self):
        return self.item_name