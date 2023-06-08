from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.

@login_required
def home(request):
    return render(request, 'imageprocess.html')

def registerUser(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'register.html', context)