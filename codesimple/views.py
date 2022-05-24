from django.shortcuts import render, reverse
from django.views import generic
from .forms import CustomUserCreationForm

# Create your views here.
def home_page(request):
    return render(request, "codesimple/home_page.html")


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    def get_success_url(self):
        return reverse("login")
