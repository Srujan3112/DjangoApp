from django.views.generic.edit import DeleteView
from ..models import Product
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from Cart.models import Cart


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'Base/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        context['quantity'] = cart.quantity
        return context
