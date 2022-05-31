"""codemadesimple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from codesimple.views import SignupView, home_page, blogNew, blogList, listMyBlogs, blogDetailView, blogDeletelView, justCheking
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', home_page.as_view(), name = 'home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name= "logout"),
    path('myblogs/', blogNew, name="myblogs"),
    path('home/', blogList, name = "home"),
    path('listmyblogs/', listMyBlogs, name='listmyblogs'),
    path('home/<int:pk>/', blogDetailView, name = 'blog-detail'),
    path('home/<pk>/delete', blogDeletelView, name = 'blog-delete'),
    path('random/', justCheking, name = "random"),

]

