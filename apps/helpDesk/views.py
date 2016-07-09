from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from apps.helpDesk.form import TrabajosForm,TrabajadorForm
from apps.helpDesk.models import Trabajo

# Create your views here.

def index(request):
    return render(request,'helpDesk/login.html')

def  trabajadores(request):
    form = TrabajadorForm

    if request.method == 'POST':
        form = TrabajadorForm(request.Post)
        if form.is_valid():
            form.save()
        return redirect('helpDesk:usuarios')
    else:
        form = TrabajadorForm


    return render(request,'helpDesk/trabajador.html',{'form':form})


def trabajosCrear(request):
    if request.method == 'POST':
        form = TrabajosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('helpDesk:trabajos')
    else:
        form = TrabajosForm()
    return render(request,'helpDesk/TrabajosForm.html',{'form':form})

def trabajos(request):
    trabajos = Trabajo.objects.all()
    contexto ={
        'trabajos':trabajos
    }
    return render(request,'helpDesk/trabajos.html',contexto)

