from django.db import models
from django.contrib.auth.models import User
from Base.models import Product
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.username)


class CartItem(models.Model):
    ordered = models.BooleanField(default=False, blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        if self.user.username and self.product.title:
            return str(self.user.username) + " " + str(self.product.title)
        else:
            return "TestUser"+" "+"TestTitle"




@receiver(pre_save, sender=CartItem)
def updater(sender, **kwargs):
    cart_item = kwargs['instance']
    try:
        id_val=cart_item.product.id
        product_instance = Product.objects.get(id=id_val)
        cart_item.price = cart_item.quantity * product_instance.price
        cart_item.ordered = True
    except:
        pass

