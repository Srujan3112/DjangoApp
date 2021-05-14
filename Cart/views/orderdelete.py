from django.views.generic.edit import DeleteView
from ..models import Order
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'Cart/order_delete.html'
    context_object_name = 'order'
    success_url = reverse_lazy('products')
