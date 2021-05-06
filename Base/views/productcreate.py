from django.views.generic.edit import CreateView
from ..models import Product
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'base/product_create.html'
    fields = ['title', 'description', 'image', 'price', 'category']
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductCreate, self).form_valid(form)
