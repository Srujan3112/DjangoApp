from django.views.generic.edit import DeleteView
from ..models import Product
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'Base/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products')
