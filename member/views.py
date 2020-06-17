from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('login successfully'))
            return redirect('home')
        else:
            messages.success(request, ('invalid details'))

    template = 'login.html'
    context = {}
    return render(request, template, context)


def logout_user(request):
    logout(request)
    messages.success(request, ('Logged out'))
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
        messages.success(request, ("User Created Successfully...Login Now"))
        return redirect('login')
    else:
        form = SignUpForm()

    template = "register.html"
    context = {"form": form}
    return render(request, template, context)
