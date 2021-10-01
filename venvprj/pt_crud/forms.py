from django import forms
from .models import Paciente


class PatientForm(forms.ModelForm):

    class Meta:
        model = Paciente
        # fields = ("",)
        fields = '__all__'
        labels =   {
            'nacimiento_fecha':'Fecha de Nacimiento',
            'documento_numero':'Número de Documento',
            'documento_tipo':'Tipo de Documento',
            'genero':'Género',
            'direccion':'Dirección',
            'obra_social':'Obra Social',
            'afiliado':'Identificación como Afiliado',
            'telefono_1':'Línea Telefónica',
            'telefono_2':'Línea Alternativa',
            'profesion':'Profesión',
            'referente':'Profesional Referente'
        }
