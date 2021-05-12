from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from Cart.models import Cart
from Base.models import Product


class CategoryList(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'categoryItems'
    template_name = 'base/specific_category.html'
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.kwargs.get('pk')
        if search:
            queryset = Product.objects.filter(category__id=search)
            return queryset
        else:
            return queryset.none()
