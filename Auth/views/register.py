from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login


class RegisterPage(FormView):
    template_name = 'Auth/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is None:
            redirect('register')
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('products')
        return super(RegisterPage, self).get(*args,**kwargs)

