from django.views.generic.list import ListView
from ..models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'base/product_list.html'
    paginate_by =8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['products'] = context['products'].filter(user=self.request.user)
        context['count'] = context['products'].count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['products'] = context['products'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        return context
