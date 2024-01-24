import logging

from core.settings.base import AUTH_USER_MODEL
from core_apps.profiles.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.info(f"{instance}'s profile created.")
