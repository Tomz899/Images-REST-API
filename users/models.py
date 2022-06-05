from django.db import models
from django.contrib.auth.models import AbstractUser


"""
Defining custom AbstractUser class for creating user tiers
"""


class TierUser(AbstractUser):
    is_basic = models.BooleanField("Basic Tier", default=True)
    is_premium = models.BooleanField("Premium Tier", default=False)
    is_enterprise = models.BooleanField("Enterprise Tier", default=False)
