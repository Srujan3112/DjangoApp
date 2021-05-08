from django.views.generic.list import ListView
from ..models import CartItem
from django.contrib.auth.mixins import LoginRequiredMixin


class CartItemsList(LoginRequiredMixin, ListView):
    model = CartItem
    context_object_name = 'cart_products'
    template_name = 'Cart/cartitems_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_products'] = context['cart_products'].filter(user=self.request.user)
        context['count'] = context['cart_products'].count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['cart_products'] = context['cart_products'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        return context
