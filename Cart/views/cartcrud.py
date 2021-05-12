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
            cart_items = CartItem.objects.filter(user=request.user, cart=cart.id)
            total_price = 0
            for items in cart_items:
                total_price += (items.product.price * items.quantity)
            cart.total_price = total_price
            quantity = cart_items.count()
            cart.quantity = quantity
            cart.save()
            return redirect('/')
    form = CartItemForm(
        initial={'user': request.user, 'price': product.price, 'product': product, 'ordered': False, 'cart': cart})
    context = {'form': form, 'user': request.user.username, 'title': product.title, 'image': product.image.url,
               'total_price': cart.total_price,'quantity':cart.quantity}

    return render(request, 'Cart/order_form.html', context)


def updateCartItem(request, pk):
    product = Product.objects.get(id=pk)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItem.objects.get(product=product.id, user=request.user)
    form = CartItemForm(instance=cart_item)
    if request.method == 'POST':
        form = CartItemForm(request.POST, instance=cart_item)
        form.save()
        cart_items = CartItem.objects.filter(user=request.user, cart=cart.id)
        quantity = cart_items.count()
        cart.quantity = quantity
        cart.save()
        return redirect('/')
        # if form.is_valid():
    context = {'form': form,'quantity':cart.quantity}
    print(form)
    return render(request, 'Cart/order_form.html', context)


def deleteCartItem(request, pk):
    product = Product.objects.get(id=pk)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItem.objects.get(product=product.id, user=request.user)
    if request.method == "POST":
        cart_item.delete()
        cart_items = CartItem.objects.filter(user=request.user, cart=cart.id)
        quantity = cart_items.count()
        cart.quantity = quantity
        cart.save()
        return redirect('/')

    context = {'item': cart_item,'quantity':cart.quantity}
    return render(request, 'Cart/delete.html', context)
