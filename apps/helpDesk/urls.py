from django.conf.urls import url, include
from apps.helpDesk.views import (
        index,
        trabajadores,
        trabajos,
        trabajosCrear,
        estados,
        clientes,
)
urlpatterns = [
    url(r'^$',index), 
    url(r'^user$',trabajadores,name='usuarios'),
    url(r'^estados$',estados,name='status'), 
    url(r'^clientes$',clientes,name='cliente'), 
    url(r'^trabajos$', trabajos, name='trabajos'), 
    url(r'^nuevo$', trabajosCrear, name='trabajosCrear'), 
    
]
