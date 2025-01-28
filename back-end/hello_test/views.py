from django.shortcuts import render
from django.http import HttpResponse

def hello1(request):
    return HttpResponse("Saaalluut 1")

def hello2(request):
    return HttpResponse("Saaalluut 2")

def hello3(request):
    return HttpResponse("Saaalluut 3")