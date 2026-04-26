from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, WishForm
from .models import Wish, Wishlist

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def examples_view(request):
    return render(request, 'examples.html')

def getstarted_view(request):
    return render(request, 'getstarted.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Wishlist.objects.get_or_create(user=user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def account_view(request):
    wishes = Wish.objects.filter(user=request.user).order_by('-created_at')
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'account.html', {
        'wishes': wishes,
        'wishlist': wishlist
    })

@login_required
def add_wish(request):
    if request.method == 'POST':
        form = WishForm(request.POST)
        if form.is_valid():
            wish = form.save(commit=False)
            wish.user = request.user
            wish.save()
            return redirect('account')
    else:
        form = WishForm()
    return render(request, 'add_wish.html', {'form': form, 'action': 'Додати'})

@login_required
def edit_wish(request, id):
    wish = get_object_or_404(Wish, id=id, user=request.user)
    if request.method == 'POST':
        form = WishForm(request.POST, instance=wish)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = WishForm(instance=wish)
    return render(request, 'add_wish.html', {'form': form, 'action': 'Зберегти зміни'})

@login_required
def delete_wish(request, id):
    wish = get_object_or_404(Wish, id=id, user=request.user)
    wish.delete()
    return redirect('account')

def public_wishlist(request, uuid):
    wishlist = get_object_or_404(Wishlist, share_link=uuid)
    wishes = Wish.objects.filter(user=wishlist.user).order_by('-created_at')
    return render(request, 'public_wishlist.html', {
        'owner': wishlist.user,
        'wishes': wishes
    })