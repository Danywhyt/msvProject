from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from apps.helpDesk.form import TrabajosForm,TrabajadorForm, EstadoForm, ClienteForm

from apps.helpDesk.models import Trabajo,Trabajador,Estados,Cliente

# Create your views here.

def index(request):
    return render(request,'helpDesk/login.html')

def  trabajadores(request):
    form = TrabajadorForm

    if request.method == 'POST':
        form = TrabajadorForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('helpDesk:usuarios')
    else:
        form = TrabajadorForm
    trabajadores = Trabajador.objects.all()
    contexto ={
        'trabajadores':trabajadores,
        'form':form
    }
    return render(request,'helpDesk/trabajador.html',contexto)


def estados(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('helpDesk:status')
    else:
        form = EstadoForm()
    estados = Estados.objects.all()
    contexto = {
        'form':form,
        'estados':estados,
    }
    return render(request,'helpDesk/status.html',contexto)
    
def clientes(request):
    if request.method=='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('helpDesk:cliente')
    else:
        form = ClienteForm()
    clientes = Cliente.objects.all()
    contexto = {
        'form':form,
        'clientes':clientes,
    }
    return render(request,'helpDesk/cliente.html',contexto)


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

