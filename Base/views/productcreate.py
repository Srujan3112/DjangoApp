from django.views.generic.edit import CreateView
from ..models import Product
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from Cart.models import Cart


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'base/product_create.html'
    fields = ['title', 'description', 'image', 'price', 'category', 'quantity']
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        context['quantity'] = cart.quantity
        return context
