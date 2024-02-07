from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePage(request):
    return render(request, 'homepage.html')

def resumePage(request):
    return render(request, 'resume.html')