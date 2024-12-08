from django.shortcuts import render
from django.http import HttpResponse

def landing_page(request):
    return HttpResponse("Testing landing page")

# Create your views here.
