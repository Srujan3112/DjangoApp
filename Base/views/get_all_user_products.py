from django.views.generic.list import ListView
from ..models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from Cart.models import Cart


class GetAllUserProducts(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'Base/get_all_user_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = context['products'].filter(user=self.request.user)
        context['count'] = context['products'].count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['products'] = context['products'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        context['quantity'] = cart.quantity
        return context
