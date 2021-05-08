from django.shortcuts import render
from django.db.models.signals import pre_save
from django.dispatch import receiver
from Cart.models import CartItem, Cart


def temp(request):
    return render(request, 'Base/basic.html')


@receiver(pre_save, sender=CartItem)
def updater(sender, **kwargs):
    # print(kwargs)
    cart_item = kwargs['instance']
    cart, _ = Cart.objects.get_or_create(user=cart_item.user)
    cart_items = CartItem.objects.filter(user=cart_item.user, cart=cart.id)
    quantity = cart_items.count()
    print(quantity)
    cart.quantity = quantity
    print(cart.quantity)
    cart.save()

