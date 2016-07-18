from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.helpDesk.views import (
        index,
        trabajadores,
        trabajos,
        trabajosCrear,
        estados,
        clientes,
        trabajosEdit,
        trabajosFinish,
        msv,
        bitacora,
        cliente_Datos,
)
urlpatterns = [
    url(r'^$',msv, name= 'msv'),
    url(r'^user$',trabajadores,name='usuarios'),
    url(r'^estados$',estados,name='status'),
    url(r'^clientes$',clientes,name='cliente'),     
    url(r'^trabajos$',trabajos, name='trabajos'), 
    url(r'^nuevo$', trabajosCrear, name='trabajosCrear'),
    url(r'^edit/(?P<id_trabajo>\d+)/$', trabajosEdit, name='trabajosEdit'), 
    url(r'^finalizar/(?P<id_trabajo>\d+)/$', trabajosFinish, name='trabajosFinish'),
    
    url(r'^bitacora/(?P<id_trabajo>\d+)/$', bitacora, name='bitacora'),

    url(r'^cliente/j/(?P<rif_cliente>\d+)/$', cliente_Datos, name='buscando'),
]

