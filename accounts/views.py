from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect("home")
    return render(request, "register.html", {"form": form})


def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = auth.authenticate(
                request,
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password"),
            )
            if user is not None:
                auth.login(request, user)
                return redirect("home")
    return render(request, "login.html", {"form": form})


def logout(request):
    auth.logout(request)
    return redirect("home")
