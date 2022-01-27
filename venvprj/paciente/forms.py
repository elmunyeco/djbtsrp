from django import forms
from .models import Paciente
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div,    Field


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        # fields = ("",)
        fields = '__all__'
        labels = {
            'nacimientofecha': 'Fecha de Nacimiento',
            'documentonumero': 'Número de Documento',
            'documentotipo': 'Tipo de Documento',
            'genero': 'Género',
            'direccion': 'Dirección',
            'obraSocial': 'Obra Social',
            'afiliado': 'Identificación como Afiliado',
            'telefonocelular': 'Teléfono celular',
            'telefonofijo': 'Teléfono Fijo',
            'profesion': 'Profesión',
            'referente': 'Profesional Referente'
        }

    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Field('div_id_nombre', css_class='col-md-3'),
                Field('apellido', css_class='col-md-9'),
                css_class='form-row'),
        )

        self.fields['nacimientofecha'].required = False
        self.fields['documentonumero'].required = False
        self.fields['documentotipo'].required = False
        self.fields['direccion'].required = False
        self.fields['localidad'].required = False
        self.fields['obrasocial'].required = False
        self.fields['plan'].required = False
        self.fields['afiliado'].required = False
        self.fields['telefonocelular'].required = False
        self.fields['telefonofijo'].required = False
        self.fields['email'].required = False
        self.fields['profesion'].required = False
        self.fields['referente'].required = False
