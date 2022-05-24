from django.shortcuts import render, reverse
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.
class home_page(LoginRequiredMixin, TemplateView):
    template_name = "codesimple/home_page.html"


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    def get_success_url(self):
        return reverse("login")
