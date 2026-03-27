from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm

def home_view(request):
    return render(request, 'home.html')
def about_view(request):
    return render(request, 'about.html')

def examples_view(request):
    return render(request, 'examples.html')

def getstarted_view(request):
    return render(request, 'getstarted.html')

@login_required
def account_view(request):
    return render(request, 'account.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})