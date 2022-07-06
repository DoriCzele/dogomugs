from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from accounts.forms import RegisterForm


def register(request):
    """View to handle user registration form submission.

    Page only visible to non-authenticated users.
    Display register template with embedded form on the GET request.
    On form POST, check data validity against model.
    If form data is valid:
    - Create new model instance
    - Log the user in
    - Redirect to homepage
    """
    if request.user.is_authenticated:
        messages.error(
            request, "You are already logged in.")
        return redirect("home")
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, "Registration successful!")
            auth.login(request, user)
            return redirect("home")
    return render(request, "register.html", {"form": form})


def login(request):
    """View to handle user login form submission.

    Page only visible to non-authenticated users.
    Display login template with embedded form on the GET request.
    On form POST, check data validity against model.
    If form data is valid:
    - Check user credentials against credentials stored in database
    - Log the user in
    - Redirect to homepage
    """
    if request.user.is_authenticated:
        messages.error(
            request, "You are already logged in.")
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
                messages.success(
                    request, "Welcome back!")
                return redirect("home")
    return render(request, "login.html", {"form": form})


def logout(request):
    """View to log the user out.

    Remove the user session cookie on request.
    Redirect to the homepage.
    """
    auth.logout(request)
    return redirect("home")
