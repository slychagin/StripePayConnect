from django.db import models
from django.urls import reverse


class Item(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)

    def get_urls(self):
        return reverse('buy_item', args=[self.pk])

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    def __str__(self):
        return self.name
