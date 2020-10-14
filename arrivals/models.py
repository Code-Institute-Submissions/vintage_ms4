from django.db import models


class Arrivals(models.Model):

    product_id = models.IntegerField(null=False, blank=False, default=0)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image1 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
