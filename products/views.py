from django.http import HttpResponse
from urllib import request
from django.shortcuts import render

# Create your views here.


def get_home(request):
    return HttpResponse(f"<h1> Hey, Welcome to our website!</h1>")