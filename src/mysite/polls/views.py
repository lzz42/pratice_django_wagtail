from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello you're at polls index")

def admin(request):
    return HttpResponse("helle this is Admin")
