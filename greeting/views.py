"""Views for the greeting app."""
from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    """Handle the greeting page request."""
    return render(request, 'index.html', {'greeting': 'Hello'})
