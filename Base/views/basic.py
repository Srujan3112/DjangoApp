from django.shortcuts import render
from django.db.models.signals import pre_save
from django.dispatch import receiver
from Cart.models import CartItem, Cart


def temp(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    context = {'quantity': cart.quantity}
    return render(request, 'Base/basic.html',context)
