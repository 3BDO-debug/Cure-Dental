
from django.db import models
from pyfcm import FCMNotification
# Create your models here.
class Notification(models.Model):
    notification_title = models.CharField(max_length=350, verbose_name="Notification Title")
    notificaiton_body = models.CharField(max_length=350, verbose_name="Notification Body")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return self.notification_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        push_service = FCMNotification(api_key="AAAA18_HQk4:APA91bFvPri5SWi3-xrd2lbY7wOOzEBTeJMcojulH9YEjJfxwN0XorhXMQbYRBG2cO9yN28lLpGwXzvif5UBuqNFZgvXRxx5Mn0hl0DsWMPhNF_ezF_1eT0ONJKJEaS5GQNAwZfGqaiR")
        registration_id = "/topics/AllDevices"
        message_title = self.notification_title
        message_body = self.notificaiton_body
        result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
        print(result)
