"""proMSV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings

from django.conf.urls import url,include

from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import login,logout_then_login
from apps.helpDesk.views import ClienteAutoComplete, msv
from  django.contrib.auth.decorators import login_required

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    url(r'^helpDesk/',include('apps.helpDesk.urls',namespace='helpDesk')),
    url(r'^usuario/',include('apps.usuario.urls',namespace='usuario')),
    url(r'^accounts/login/',login,{'template_name':'usuario/index.html'},name='loginUser'),
    url(r'^logout/',logout_then_login, name='logout'),

    url(r'^clienteComplete/$', ClienteAutoComplete.as_view(), name='clienteComplete'),
    url(r'^$',msv,name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)