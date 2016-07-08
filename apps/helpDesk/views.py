from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'helpDesk/login.html')

def trabajos(request):
    return render(request,'helpDesk/trabajos.html')