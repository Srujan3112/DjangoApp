from django.db import models
from .categorie import Categorie
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')
    price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
