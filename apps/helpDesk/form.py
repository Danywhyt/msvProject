from django import  forms
from apps.helpDesk.models import Trabajo,Trabajador,Estados,Cliente,Bitacora


class  TrabajosForm(forms.ModelForm):
    
    class Meta:
        model = Trabajo

        fields=[
            'id_cliente',
            'fechaVisita',
            'observacion',
            'cobrado',
            'status',
            'id_trabajador',

        ]

        labels = {
            
            'id_cliente':'Cliente',
            'fechaVisita':'Fecha Visita',
            'status':'Estado',
            'observacion':'Observacion',
            'cobrado':'Cobrado',
            'id_trabajador':'Trabajador',
        }
        widgets = {
            
            'id_cliente':forms.Select(attrs={'class':'form-control',}),
            'fechaVisita':forms.DateInput(attrs={'class':'form-control','type':'date'}) ,
            'status':forms.CheckboxInput(attrs={'class':'form-control','checked':'true'}),
            'observacion':forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'cobrado':forms.CheckboxInput(attrs={'class':'form-control'}),
            'id_trabajador':forms.Select(attrs={'class':'form-control'}),
        }


class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador

        fields = [
            'nombre',
            'clave',
            'numero'
        ]

        labels = {
            'nombre':'Nombre',
            'clave':'Clave',
            'numero':'Numero',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'clave':forms.TextInput(attrs={'class':'form-control','type':'password','placeholder':'Clave'}),
            'numero':forms.NumberInput(attrs={'class':'form-control','placeholder':'Numero'}),
        }

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estados
        fields = [ 'nombre']
        labels = {
            'nombre':'nombre',
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'})
        }

class ClienteForm(forms.ModelForm):
    class Meta():
        model = Cliente

        fields = [
            'nombre',
            'rif',
            'numero',
            'direccion',
        ]

        labels = {
            'nombre':'Nombre',
            'rif':'Rif',
            'numero':'Numero',
            'direcion':'Direccion',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
            'rif':forms.TextInput(attrs={'class':'form-control','placeholder':'RIF'}),
            'numero':forms.NumberInput(attrs={'class':'form-control','placeholder':'Numero'}),
            'direccion':forms.Textarea(attrs={'class':'form-control','placeholder':'Direccion','rows':'1','max-height':'50px'}),
           
        }        


class BitacoraForm(forms.ModelForm):
    class Meta:
        model = Bitacora
        fields=[
            'comentario',
            'monto',
            'id_trabajador',
            'id_trabajo',
            'id_estado',
        ]
        labels={
            'comentario': 'Comentario',
            'monto': 'Monto',
            'id_trabajador':'Trabajador',
            'id_trabajo':'Cliente',
            'id_estado':'Estado',
            }

        widgets={
            
        'comentario':forms.Textarea(attrs={'class':'form-control','placeholder':'Cometario','rows':'1'}),
        'monto': forms.NumberInput(attrs={'class':'form-control','placeholder':'Monto'}),
        'id_trabajador':forms.SelectMultiple(attrs={'class':'form-control'}),
        'id_trabajo':forms.Select(attrs={'class':'form-control'}),
        'id_estado':forms.Select(attrs={'class':'form-control'}),
        }