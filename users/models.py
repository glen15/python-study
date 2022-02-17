from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """Custon User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    RANK_NEWB = "newb"
    RANK_SILVER = "silver"
    RANK_GOLD = "gold"
    RANK_MASTER = "master"
    RANK_CHOICES = (
        (RANK_NEWB, "Newb"),
        (RANK_SILVER, "Silver"),
        (RANK_GOLD, "Gold"),
        (RANK_MASTER, "Master"),
    )
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    rank = models.CharField(
        ddefault="Newb", choices=RANK_CHOICES, max_length=10, null=True
    )
    bio = models.TextField(default="", blank=True)
