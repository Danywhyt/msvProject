from dal import autocomplete

from django.shortcuts import render, redirect
# from django.http import HttpResponse

from apps.helpDesk.form import TrabajosForm, TrabajadorForm, EstadoForm, ClienteForm, BitacoraForm
from apps.helpDesk.models import Trabajo, Trabajador, Estados, Cliente, Bitacora
from apps.usuario.models import UserProfile
from apps.usuario.form import RegUserForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


class ClienteAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        if not self.request.user.is_authenticated():
            return Cliente.objects.none()

        qs = Cliente.objects.all()

        if self.q:
            qs = qs.filter(rif__istartswith=self.q)

        return qs


def index(request):
        return render(request, 'helpDesk/login.html')


@login_required
def trabajadores(request):
    
    form2 = RegUserForm
    #form = TrabajadorForm

    usuario = User.objects.all()
        
    if request.method == 'POST':
        print('--------------Test REgistro Usuario-----------------')
        form2 = RegUserForm(request.POST or None)
        if form2.is_valid():
            cleaned_data = form2.cleaned_data
            password = cleaned_data.get('password')
            username = cleaned_data.get('username')
            email = cleaned_data.get('email')
            nombre = cleaned_data.get('nombre')
            numero = cleaned_data.get('numero')
            user_model = User.objects.create_user(username=username, password=password)
            user_model.email = email
            user_model.save()
            user_profile = UserProfile()
            user_profile.user = user_model
            user_profile.nombre = nombre
            user_profile.numero = numero
            user_profile.save()
            return redirect('helpDesk:trabajos')
        else:
            form2 = RegUserForm()

            
    #     form = TrabajadorForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('helpDesk:usuarios')
    # else:
    #     form = TrabajadorForm

    trabajadores = Trabajador.objects.all()
    contexto = {
        'trabajadores': trabajadores,
        'form2': form2,
        'usuario': usuario,
    }
    return render(request, 'helpDesk/trabajador.html', contexto)

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

            print(rif_cliente)
            cliente = Cliente.objects.get(rif=rif_cliente)
            trabajos = Trabajo.objects.filter(id_cliente__rif=rif_cliente)
            # print (cliente)
            # print (trabajos)
            
            context = {
                'cliente': cliente,
                'trabajos': trabajos
            }
            return redirect ('helpDesk:buscando', rif_cliente1)
            # return render (request,'helpDesk/clienteTrabajos.html',{'rif_cliente':rif_cliente})

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

    print('Entrando en la View')
    if request.method == 'POST':
        form = TrabajosForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_cliente = Cliente.objects.get(pk=request.POST['id_cliente'])
            post.id_trabajador = User.objects.get(pk=request.user.id)
            post.status = False
            post.cobrado = False
            form.save()
        else:
            return redirect('helpDesk:trabajosCrear')
        return redirect('helpDesk:trabajos')
    else:
        form = TrabajosForm()
    return render(request, 'helpDesk/TrabajosForm.html', {'form': form})


@login_required
def trabajos(request):

    trabajos = Trabajo.objects.filter(status=False)
    # estados = Bitacora.objects.filter(trabajos__status=False)
    estados = Bitacora.objects.filter(id_trabajo__status=False)
    # estados = Trabajo.objects.filter()
    
    if request.method=='POST':
        # print (request.GET['rif_j'])
        # print (request.GET[])
        
        print(request.POST['nRif'])
        #redirect ('helpDesk:buscando', id_cliente )

        rif_cliente = request.POST['buscar-rif']

        return redirect('helpDesk:buscando', rif_cliente)

        # for i in estados:
        # print (str(i.id_trabajo.id) + '--->BITACORA')
        # print (str(i.id_estado.nombre) + '--->')

    contexto = {
        'trabajos': trabajos,
        'estados': estados,
    }
    return render(request, 'helpDesk/trabajos.html', contexto)


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
    
    return render(request, 'helpDesk/trabajosForm.html', {'form': form})


@login_required
def trabajosFinish(request,id_trabajo):

    trabajo = Trabajo.objects.get(id=id_trabajo)
    form = Trabajo.objects.all()
    if request.method == 'GET':
        if trabajo.status:
            trabajo.status = False
        else:
            trabajo.status = True
            
        trabajo.save()
        print(trabajo.status)
    
    return redirect('helpDesk:trabajos')


@login_required
def msv(request):

    trabajos = Trabajo.objects.all()
    
    contexto = {
        'trabajos': trabajos
    }
    return render(request, 'helpDesk/trabajos.html', contexto)


@login_required
def bitacora(request, id_trabajo):
    
    cliente = Trabajo.objects.get(id=id_trabajo)
    
    trabajo = Bitacora.objects.filter(id_trabajo=id_trabajo)

    estado = Trabajo.objects.filter(id=id_trabajo)

    # print(estado)
    if request.method == 'POST':
        form = BitacoraForm(request.POST)
        print(request.POST)
        # print(form)
        # print (cliente)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_trabajo = cliente
            post.id_trabajador = User.objects.get(pk = request.POST['id_trabajador'])

            estado.update(id_estado=request.POST['id_estado'])
            #print('--------------------------------------------------------------')
            #print (cliente.observacion)
            estado.update(observacion=request.POST['comentario'])

            form.save()

            return redirect('helpDesk:bitacora', id_trabajo)
    else:
        form = BitacoraForm()
    contexto = {
        'cliente': cliente,
        'form': form,
        'trabajo': trabajo,
        'estado':estado,
    }
    
    return render(request, 'helpDesk/bitacora.html', contexto)


@login_required
def cliente_Datos(request,rif_cliente):

    rif_cliente = 'J' + rif_cliente
    # print (rif_cliente)
    cliente = Cliente.objects.get(rif=rif_cliente)
    trabajos = Trabajo.objects.filter(id_cliente__rif=rif_cliente)
    # print (cliente)
    # print (trabajos)
    
    context = {
        'cliente': cliente,
        'trabajos': trabajos,
     }

    return render(request, 'helpDesk/clienteTrabajos.html', {'rif_cliente': rif_cliente})
