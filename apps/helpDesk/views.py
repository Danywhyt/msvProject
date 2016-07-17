from django.shortcuts import render, redirect
# from django.http import HttpResponse

from apps.helpDesk.form import TrabajosForm, TrabajadorForm, EstadoForm, ClienteForm, BitacoraForm

from apps.helpDesk.models import Trabajo, Trabajador, Estados, Cliente, Bitacora
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
        return render(request, 'helpDesk/login.html')

@login_required
def trabajadores(request):

    form = TrabajadorForm
    usuario = User.objects.all()
    if request.method == 'POST':
        form = TrabajadorForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('helpDesk:usuarios')
    else:
        form = TrabajadorForm
    trabajadores = Trabajador.objects.all()
    contexto = {
        'trabajadores': trabajadores,
        'form': form,
        'usuario': usuario,
    }
    return render(request,'helpDesk/trabajador.html',contexto)

@login_required
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

@login_required
def clientes(request):
    
    if request.method=='POST':
        if "nRif" in request.POST:
            print (request.POST)
            rif_cliente1 = request.POST['buscar-rif']
            rif_cliente = 'J' + rif_cliente1

            print (rif_cliente)
            cliente = Cliente.objects.get(rif=rif_cliente)
            trabajos = Trabajo.objects.filter(id_cliente__rif=rif_cliente)
            #print (cliente)
            #print (trabajos)
            
            context ={
                'cliente':cliente,
                'trabajos':trabajos
            }
            return redirect ('helpDesk:buscando', rif_cliente1)
            #return render (request,'helpDesk/clienteTrabajos.html',{'rif_cliente':rif_cliente})
            
                
        if 'cliente-form' in request.POST:
                
            
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

@login_required
def trabajosCrear(request):
    if request.method == 'POST':
        form = TrabajosForm(request.POST)   
        if form.is_valid():
            post = form.save(commit=False)
            post.id_trabajador = request.user.id 
            form.save()
        else:
            return redirect('helpDesk:trabajosCrear')
        return redirect('helpDesk:trabajos')
    else:
        form = TrabajosForm()
    return render(request,'helpDesk/TrabajosForm.html',{'form':form})


@login_required
def trabajos(request):
    trabajos = Trabajo.objects.filter(status=False)
    #estados = Bitacora.objects.filter(trabajos__status=False)
    estados = Bitacora.objects.filter(id_trabajo__status=False)
    #estados = Trabajo.objects.filter()
    


    if request.method=='POST':
        #print (request.GET['rif_j'])
        #print (request.GET[])
        
        print(request.POST['nRif'])
        #redirect ('helpDesk:buscando', id_cliente )

        rif_cliente =  request.POST['buscar-rif']

        return redirect ('helpDesk:buscando', rif_cliente)



        #for i in estados:
        #print (str(i.id_trabajo.id) + '--->BITACORA')
        #print (str(i.id_estado.nombre) + '--->')
       
        
    contexto = {
        'trabajos':trabajos,
        'estados':estados,
    }
    return render(request,'helpDesk/trabajos.html',contexto)




@login_required
def trabajosEdit(request,id_trabajo):
    trabajo = Trabajo.objects.get(id=id_trabajo)
    if request.method == 'GET':
        form = TrabajosForm(instance=trabajo)
    else:
        form = TrabajosForm(request.POST,instance = trabajo)
        if form.is_valid():
            form.save()
        return redirect('helpDesk:trabajos')
    
    return render(request,'helpDesk/trabajosForm.html',{'form':form})
@login_required
def trabajosFinish(request,id_trabajo):
    trabajo = Trabajo.objects.get(id=id_trabajo)
    form = Trabajo.objects.all()
    
    if request.method== 'GET':
        if trabajo.status:
            trabajo.status = False
        else:
            trabajo.status = True
            
        trabajo.save()
        print (trabajo.status)
    
    return redirect('helpDesk:trabajos')

@login_required
def msv(request):
    trabajos = Trabajo.objects.all()
    
    contexto = {
        'trabajos': trabajos
    }
    return render(request,'helpDesk/trabajos.html',contexto)

@login_required
def bitacora(request,id_trabajo):
    
    cliente = Trabajo.objects.get(id= id_trabajo)
    
    trabajo = Bitacora.objects.filter(id_trabajo= id_trabajo)

    estado = Trabajo.objects.filter(id= id_trabajo)
    
    #print(estado)
    if request.method == 'POST':
        form = BitacoraForm(request.POST)
        #print (request.POST['id_trabajador'])
        print(request.POST['id_estado'])
        #print (cliente)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_trabajo = cliente
            form.save()

            estado.update(id_estado=request.POST['id_estado'])

        
            return redirect('helpDesk:bitacora',id_trabajo)
    else:
        form = BitacoraForm()
    contexto ={
        'cliente':cliente,
        'form':form,
        'trabajo':trabajo,
    }
    
    return render(request,'helpDesk/bitacora.html',contexto)

@login_required
def cliente_Datos(request,rif_cliente):

    rif_cliente = 'J' + rif_cliente
    #print (rif_cliente)
    cliente = Cliente.objects.get(rif=rif_cliente)
    trabajos = Trabajo.objects.filter(id_cliente__rif=rif_cliente)
    #print (cliente)
    #print (trabajos)
    
    context ={
        'cliente':cliente,
        'trabajos':trabajos
     }

    return render (request,'helpDesk/clienteTrabajos.html',{'rif_cliente':rif_cliente})
    