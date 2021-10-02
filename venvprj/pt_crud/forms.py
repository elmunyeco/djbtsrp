from django import forms
from .models import Paciente


class PatientForm(forms.ModelForm):

    class Meta:
        model = Paciente
        # fields = ("",)
        fields = '__all__'
        labels = {
            'nacimientoFecha': 'Fecha de Nacimiento',
            'documentoNumero': 'Número de Documento',
            'documentoTipo': 'Tipo de Documento',
            'genero': 'Género',
            'direccion': 'Dirección',
            'obraSocial': 'Obra Social',
            'afiliado': 'Identificación como Afiliado',
            'telefono1': 'Línea Telefónica',
            'telefono2': 'Línea Alternativa',
            'profesion': 'Profesión',
            'referente': 'Profesional Referente'
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['nacimientoFecha'].required = False
        self.fields['documentoNumero'].required = False
        self.fields['documentoTipo'].required = False
        self.fields['direccion'].required = False
        self.fields['localidad'].required = False
        self.fields['obraSocial'].required = False
        self.fields['plan'].required = False
        self.fields['afiliado'].required = False
        self.fields['telefono1'].required = False
        self.fields['telefono2'].required = False
        self.fields['email'].required = False
        self.fields['profesion'].required = False
        self.fields['referente'].required = False
