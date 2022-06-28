from django.shortcuts import render


def home(request):
    """View to handle home template."""
    return render(request, "home.html")
