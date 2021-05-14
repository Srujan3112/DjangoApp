from django.db import models
from django.contrib.auth.models import User
from Base.models import Product
from Cart.models import CartItem
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Order(models.Model):
    order_item = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=1, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.user.username:
            return self.user.username
        else:
            return "Test Username"

    class Meta:
        ordering = ['-created']
