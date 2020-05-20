from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello you're at polls index")

def admin(request):
    return HttpResponse("helle this is Admin")

def detail(request,question_id):
    return HttpResponse("You are looking question: %s"%question_id)

def results(requst,question_id):
    rep = HttpResponse("You are looking question: %s"%question_id)
    return HttpResponse(rep%question_id)

def vote(resquest,question_id):
    return  HttpResponse("You are vating on question: %s"%question_id)
