from django.views.generic.list import ListView
from ..models import CartItem, Cart
from Cart.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderItems(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'order_items'
    template_name = 'Cart/order_listing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        cart_items = CartItem.objects.filter(user=self.request.user, cart=cart.id)
        if self.request.GET.get('choice') == 'True':
            for item in cart_items:
                orderitem, _ = Order.objects.get_or_create(order_item=item.product, user=self.request.user,
                                                           quantity=item.quantity)
                orderitem.save()
            try:
                CartItem.objects.filter(user=self.request.user).delete()
            except:
                pass
            quantity = cart_items.count()
            cart.quantity = quantity
            cart.save()
        order_items = Order.objects.filter(user=self.request.user)
        cart_items = CartItem.objects.filter(user=self.request.user, cart=cart.id)
        context['order_items'] = order_items
        context['quantity'] = cart_items.count()
        context['count'] = order_items.count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['order_items'] = context['order_items'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        return context
