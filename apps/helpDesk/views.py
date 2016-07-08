from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from apps.helpDesk.form import TrabajosForm

# Create your views here.

def index(request):
    return render(request,'helpDesk/login.html')

def trabajos(request):
    return render(request,'helpDesk/trabajos.html')

def trabajosCrear(request):
    if request.method == 'POST':
        form = TrabajosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('helpDesk:trabajos')
    else:
        form = TrabajosForm()
    return render(request,'helpDesk/TrabajosForm.html',{'form':form})