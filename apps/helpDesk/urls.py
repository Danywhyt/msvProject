from django.conf.urls import url, include
from apps.helpDesk.views import index,trabajos
urlpatterns = [
    url(r'^$',index), 
    url(r'^trabajos$',trabajos), 
    
]
