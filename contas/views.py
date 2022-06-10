from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class CriarConta(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'contas/html/registrar.html'

