from django.shortcuts import render, redirect
from Base.models import Product
from django.urls import reverse_lazy
from ..models import CartItem, Cart
from ..forms import CartItemForm
from django.contrib.auth.models import User
from Base.models import Product


def createCartItem(request, pk):
    product = Product.objects.get(id=pk)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    if CartItem.objects.filter(user=request.user, ordered=False, product=product.id).exists():
        return redirect('/')
    form = CartItemForm()
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    total_price = 0
    cart_items = CartItem.objects.filter(user=request.user, cart=cart.id)
    for items in cart_items:
        total_price += items.price
    cart.total_price = total_price
    cart.save()
    form = CartItemForm(
        initial={'user': request.user, 'price': product.price, 'product': product, 'ordered': False, 'cart': cart})
    context = {'form': form, 'user': request.user.username, 'title': product.title, 'image': product.image.url,
               'total_price': total_price}
    return render(request, 'Cart/order_form.html', context)


def updateCartItem(request, pk):
    product = Product.objects.get(id=pk)
    cart_item = CartItem.objects.get(product=product.id, user=request.user)
    form = CartItemForm(instance=cart_item)

    if request.method == 'POST':
        form = CartItemForm(request.POST, instance=cart_item)
        form.save()
        return redirect('/')
        # if form.is_valid():
    context = {'form': form}
    return render(request, 'Cart/order_form.html', context)


def deleteCartItem(request, pk):
    product = Product.objects.get(id=pk)
    cart_item = CartItem.objects.get(product=product.id, user=request.user)
    if request.method == "POST":
        cart_item.delete()
        return redirect('/')

    context = {'item': cart_item}
    return render(request, 'Cart/delete.html', context)