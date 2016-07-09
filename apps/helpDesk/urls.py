from django.conf.urls import url, include
from apps.helpDesk.views import (
        index,
        trabajadores,
        trabajos,
        trabajosCrear,
)
urlpatterns = [
    url(r'^$',index), 
    url(r'^user$',trabajadores,name='usuarios'), 
    url(r'^trabajos$', trabajos, name='trabajos'), 
    url(r'^nuevo$', trabajosCrear, name='trabajosCrear'), 
    
]
