from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from django.contrib.auth.models import User


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'