from django.views.generic.edit import CreateView
from ..models import CartItem
from Base.models import Product
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CartItemCreateForm(ModelForm):
    class Meta:
        model = CartItem
        fields = "__all__"


class CartItemCreate(LoginRequiredMixin, CreateView):
    model = CartItem
    template_name = 'Cart/cartitem_create.html'
    form_class = CartItemCreateForm
    success_url = reverse_lazy('products')

    def get_initial(self, *args, **kwargs):
        initial = super(CartItemCreate, self).get_initial()
        product = Product.objects.get(id=self.kwargs.get("pk"))
        initial.update({'user': self.request.user, 'price': product.price, 'product': product})
        return initial

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(CartItemCreate, self).form_valid(form)
