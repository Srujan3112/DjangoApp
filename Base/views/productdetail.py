from django.views.generic.detail import DetailView
from ..models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'base/product_detail.html'
