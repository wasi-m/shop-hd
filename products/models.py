from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.URLField(blank=True)
    stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    saleprice = models.DecimalField(max_digits=8, decimal_places=2)

    def get_absolute_url(self):
        return reverse("products:view", kwargs={"pk": self.pk})

    def clean(self):
        if self.price < 0:
            raise ValidationError({"price": "Price must be greater or equal to zero."})
