
from django.conf.urls import url
from apps.usuario.views import reg_view

urlpatterns = [
    url(r'^registrar', reg_view, name='registrar'),
]
