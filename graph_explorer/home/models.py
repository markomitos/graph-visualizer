from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class CenterContent(models.Model):
    svg_content = models.TextField()

@receiver(post_save, sender=CenterContent)
def center_content_changed(sender, instance, **kwargs):
    # Notify observers about the change
    for observer in Observer.objects.all():
        print(f"Sending notification to {observer.name} at {observer.email}: Center content has been updated.")
        # Here you can implement the logic to send an email or perform any other action