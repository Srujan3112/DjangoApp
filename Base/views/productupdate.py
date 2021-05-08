from django.views.generic.edit import UpdateView
from ..models import Product
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'base/product_update.html'
    fields = ['title', 'description', 'image', 'price', 'category','quantity']
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductUpdate, self).form_valid(form)
