from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime


# Create your views here.
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        context=
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })


def contact(request):
    """Renders the view items"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        context=
        {
        })


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        context=
        {
        })
