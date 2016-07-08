from django import  forms
from apps.helpDesk.models import Trabajo


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
            
            'id_cliente':forms.Select(attrs={'class':'form-control'}),
            'fechaVisita':forms.DateInput(attrs={'class':'form-control','type':'date'}) ,
            'status':forms.CheckboxInput(attrs={'class':'form-control','checked':'true'}),
            'observacion':forms.Textarea(attrs={'class':'form-control','rows':'5'}),
            'cobrado':forms.CheckboxInput(attrs={'class':'form-control'}),
            'id_trabajador':forms.Select(attrs={'class':'form-control'}),
        }