from django.db import models

# Create your models here.
 
class Trabajo(models.Model):
    fechaHora = models.DateTimeField(auto_now_add=True)
    fechaHora = models.DateTimeField(null=True)
    status = models.BooleanField()
    observacion = models.TextField()
    cobrado = models.BooleanField()
    id_trabajador1 = models.IntegerField()
    id_cliente1 = models.IntegerField()

    def __str__(self):
        return '%s %s %s' % (self.observacion,self.user,self.cliente)
        
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    rif = models.IntegerField()
    numero = models.IntegerField()
    correo = models.EmailField()
    def __str__ (self):
        return '%s %s' % (self.nombre,self.correo)

class Bitacora(models.Model):
    fecha_estado = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()
    monto = models.IntegerField()
    id_trabajador2 = models.IntegerField()
    id_trabajo = models.IntegerField()
    id_estado = models.IntegerField()


    def __str__(self):
        return '%s' % (self.comentario)

class Estados(models.Model):
    nombre = models.CharField(max_length= 100)
    def __str__(self):
        return '%s' %(self.nombre)
        
