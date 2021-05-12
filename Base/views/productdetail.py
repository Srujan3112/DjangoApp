from django.views.generic.detail import DetailView

from Cart.models import Cart
from ..models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'base/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        context['quantity'] = cart.quantity
        return context
