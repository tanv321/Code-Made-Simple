from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.views import generic
from .forms import CustomUserCreationForm, BlogPostForm, commentForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required  #login required for function based view
from django.contrib.auth.mixins import LoginRequiredMixin  #login requied for class based views
from django.contrib import messages
from .models import BlogPost, Comment
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
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()
            return redirect("/home")
    else:
        form = BlogPostForm()
    context = { 
        "form": form 
    }
    return render(request, "codesimple/myblogs.html", context)


@login_required 
def blogList(request):
    blogs = BlogPost.objects.all()
    context = {
        "blogs":blogs
    }
    return render(request, "codesimple/home_page.html", context)



@login_required
def listMyBlogs(request):
    blogs = BlogPost.objects.filter(created_by=request.user)
    context = {
        "blogs":blogs
    }
    return render(request, "codesimple/listmyblogs.html", context)


# @login_required
# def blogDetailView(request, pk):
#     blogs = BlogPost.objects.get(id=pk)
#     context = {
#         "blogs":blogs
#     }
#     return render(request, "codesimple/blogDetailView.html", context)
@login_required
def blogDetailView(request, pk):
    blogPost = BlogPost.objects.get(id=pk)
    if request.method == "POST":
        form = commentForm(request.POST)
        user_comment = None
        if form.is_valid():
            user_comment = form.save(commit = False)
            # user_comment.blogPost = blogPost
            user_comment.post_id = pk
            user_comment.created_by = request.user

            user_comment.save()
            return redirect('/home/'+str(pk))
    else:
        form = commentForm()

 
    context = {
        "blogPost":blogPost,
        "form":form,
        "comm":Comment.objects.all()

    }
    return render(request, "codesimple/blogDetailView.html", context)



@login_required
def blogDeletelView(request, pk):
    blogs = BlogPost.objects.get(id=pk)
    if request.user == blogs.created_by:
        blogs.delete()
    return redirect("/home")


