from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Designer(models.Model):

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    designer = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
