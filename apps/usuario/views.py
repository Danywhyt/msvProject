from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from apps.usuario.models import UserProfile
from apps.usuario.form import RegUserForm


def reg_view(request):
    if request.method == 'POST':
        form = RegUserForm(request.POST)

        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            nombre = cleaned_data.get('nombre')
            numero = cleaned_data.get('numero')
            # E instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=username, password=password)
            # Añadimos el email
            user_model.email = email
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile, aunque no haya incluido
            # una imagen, ya quedara la referencia creada en la db.
            user_profile = UserProfile()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            # y le asignamos la photo (el campo, permite datos null)
            user_profile.nombre = nombre
            user_profile.numero = numero
            # Por ultimo, guardamos tambien el objeto UserProfile
            user_profile.save()
            # Ahora, redireccionamos a la pagina accounts/gracias.html
            # Pero lo hacemos con un redirect.
            return redirect('helpDesk:trabajos')
    else:
        form = RegUserForm()

    context = {
        'form':form,
    }
    return render(request, 'usuario/registro.html', context)

