
from django.conf.urls import url
from apps.usuario.views import reg_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^registrar', login_required(reg_view), name='registrar'),
]
