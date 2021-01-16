from django.db import models

# Create your models here.
class Tip(models.Model):
    tip_image = models.ImageField(verbose_name="Tip's Image")
    tip_english_text = models.TextField(verbose_name="Tip's English Text")
    tip_arabic_text = models.TextField(verbose_name="Tip's Arabic Text")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")


    class Meta:
        verbose_name = "Tip"
        verbose_name_plural = "Tips"

    def __str__(self):
        return self.tip_english_text