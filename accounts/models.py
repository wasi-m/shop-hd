from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product

class User(AbstractUser):
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False, default=None
    )

    viewed = models.ManyToManyField(
        Product, blank=True, related_name="viewed", symmetrical=False, default=None
    )

    def __str__(self):
          return f"{self.username} Profile"