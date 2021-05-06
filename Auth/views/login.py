from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'Auth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_success_url(self):
        return reverse_lazy('products')
