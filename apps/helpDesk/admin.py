from django.contrib import admin
from apps.helpDesk.models import Trabajador,Cliente,Estados,Trabajo,Bitacora

# Register your models here.

admin.site.register(Trabajador)
admin.site.register(Cliente)
admin.site.register(Estados)
admin.site.register(Trabajo)
admin.site.register(Bitacora)
