from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import (
    home_view,
    about_view,
    examples_view,
    getstarted_view,
    account_view,
    register_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('examples/', examples_view, name='examples'),
    path('getstarted/', getstarted_view, name='getstarted'),
    path('account/', account_view, name='account'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]