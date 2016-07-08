from django.conf.urls import url, include
from apps.helpDesk.views import index,trabajos,trabajosCrear
urlpatterns = [
    url(r'^$',index), 
    url(r'^trabajos$', trabajos, name='trabajos'), 
    url(r'^nuevo$', trabajosCrear, name='trabajosCrear'), 
    
]
