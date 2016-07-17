from django.db import models
from  django.contrib.auth.models import User
import datetime
# Create your models here.


class Trabajador(models.Model):
    nombre = models.CharField(max_length=150)
    clave = models.CharField(max_length= 30)
    numero = models.IntegerField()
    def __str__(self):
        return '%s %s %s' % (self.id,self.nombre,self.clave)
        
        
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    rif = models.CharField(max_length=100)
    numero = models.IntegerField()
    direccion = models.TextField()
    def __str__ (self):
        fiel= [
            self.rif,
            self.nombre,
        ]
        return 'Cliente: {:_<11.11}{:_<18.16}{:<22.20}'.format(self.rif, self.nombre, self.direccion)



class Estados(models.Model):
    nombre = models.CharField(max_length= 100)
    def __str__(self):
        return '%s' %(self.nombre)

 
class Trabajo(models.Model):
    fechaHora = models.DateTimeField(auto_now_add=True)
    fechaVisita = models.DateField(null=True,blank=True)
    status = models.BooleanField()
    observacion = models.TextField()
    cobrado = models.BooleanField()
    id_trabajador = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente,null=True,blank=True,on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estados,null=True,blank=True,on_delete=models.CASCADE,)
    def __str__(self):
        return '%s %s' % (self.pk,self.id_cliente)
        
class Bitacora(models.Model):
    fecha_estado = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()
    monto = models.IntegerField()
    id_trabajador = models.ManyToManyField(User)
    id_trabajo = models.ForeignKey(Trabajo,null=True,blank=True,on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estados,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.comentario)