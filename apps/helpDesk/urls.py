from django.conf.urls import url, include
from apps.helpDesk.views import index
urlpatterns = [
    url(r'^$',index), 
]
