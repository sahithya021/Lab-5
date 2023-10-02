from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_message(request):
    return render(request,'Message.html')