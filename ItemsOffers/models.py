from django.db import models

# Create your models here.
class ItemOffer(models.Model):
    item_english_name = models.CharField(max_length=350, verbose_name="Item Name In English")
    item_arabic_name = models.CharField(max_length=350, verbose_name="Item Name In Arabic")
    item_price = models.FloatField(verbose_name="Item Price")

    class Meta:
        verbose_name = "Item Offer"
        verbose_name_plural = "Item Offers"

    def __str__(self):
        return self.item_english_name