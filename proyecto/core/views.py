from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreateForm, UserProfileForm


# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render (request, 'core/about.html')

class Register(CreateView):
    form_class = CustomUserCreateForm
    template_name = "core/register.html"
    success_url = reverse_lazy('core:login')

class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "core/profile.html"
    success_url = reverse_lazy('core:index')

    def get_object(self):
        return self.request.user

    