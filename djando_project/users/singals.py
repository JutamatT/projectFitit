from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,review

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwaegs):
    instance.profile.save()
    instance.review.save()