from django.contrib import admin
from django.urls import path, include  # Додали include
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Головні сторінки (беруться з додатка users)
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('examples/', views.examples_view, name='examples'),
    path('getstarted/', views.getstarted_view, name='getstarted'),
    path('account/', views.account_view, name='account'),
    
    # Авторизація
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Керування бажаннями
    path('add-wish/', views.add_wish, name='add_wish'),
    path('edit-wish/<int:id>/', views.edit_wish, name='edit_wish'),
    path('delete-wish/<int:id>/', views.delete_wish, name='delete_wish'),
    
    # Публічне посилання
    path('wishlist/<uuid:uuid>/', views.public_wishlist, name='public_wishlist'),
]