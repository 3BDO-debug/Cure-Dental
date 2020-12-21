from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=350, verbose_name="Name") 
    phone = models.CharField(max_length=500, verbose_name="Phone Number")
    msg = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Sent At")
    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return self.name