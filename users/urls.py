from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('examples/', views.examples_view, name='examples'),
    path('getstarted/', views.getstarted_view, name='getstarted'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('account/', views.account_view, name='account'),
    path('add-wish/', views.add_wish, name='add_wish'),
    path('edit-wish/<int:id>/', views.edit_wish, name='edit_wish'),
    path('delete-wish/<int:id>/', views.delete_wish, name='delete_wish'),
    path('wishlist/<uuid:uuid>/', views.public_wishlist, name='public_wishlist'),
]