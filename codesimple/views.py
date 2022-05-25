from django.shortcuts import redirect, render, reverse
from django.views import generic
from .forms import CustomUserCreationForm, blogPostForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required  #login required for function based view
from django.contrib.auth.mixins import LoginRequiredMixin  #login requied for class based views
from django.contrib import messages
from .models import blogPost
# Create your views here.
class home_page(LoginRequiredMixin, TemplateView):
    template_name = "codesimple/home_page.html"


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    def get_success_url(self):
        return reverse("login")


@login_required 
def blogNew(request):
    if request.method == "POST":
        form = blogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = blogPostForm()
    context = { 
        "form": form 
    }
    return render(request, "codesimple/myblogs.html", context)

@login_required 
def blogList(request):
    blogs = blogPost.objects.all()
    context = {
        "blogs":blogs
    }
    return render(request, "codesimple/home_page.html", context)

