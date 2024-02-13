from django import forms
from .models import Paciente
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit


class PacienteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Div(
                Field('documentotipo', wrapper_class='col-md-5'),
                Field('documentonumero', wrapper_class='col-md-5'),
                css_class='row d-flex justify-content-center'
            ),
            Div(
                Field('nombre', wrapper_class='col-md-6'),
                Field('apellido', wrapper_class='col-md-6'),
                css_class='row d-flex justify-content-center'
            ),
            Div(
                Field('nacimientofecha', wrapper_class='col-md-4'),
                Field('genero', wrapper_class='col-md-4'),
                css_class='row d-flex justify-content-center'
            ),
            Div(
                Field('direccion', wrapper_class='col-md-5'),
                Field('localidad', wrapper_class='col-md-5'),
                css_class='row d-flex justify-content-center'
                
            ),
            Div(
                
                Field('telefonofijo', wrapper_class='col-md-3'),
                Field('telefonocelular', wrapper_class='col-md-3'),
                Field('email', wrapper_class='col-md-6'),
                css_class='row d-flex justify-content-center'
            ), 
            Div(
                Field('obrasocial', wrapper_class='col-md-3'),
                Field('plan', wrapper_class='col-md-3'),
                Field('afiliado', wrapper_class='col-md-6'),
                css_class='row d-flex justify-content-center'
            ),
            Div(
                Field('profesion', wrapper_class='col-md-5'),
                Field('referente', wrapper_class='col-md-5'),
                css_class='row d-flex justify-content-center'
            ),
            Div(
                Submit('submit', 'Guardar'),
                css_class='row d-flex justify-content-center'
            ),
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

    class Meta:
        model = Paciente
        fields = '__all__'
        """ fields = ('nombre', 'apellido') """
        labels = {
            'nacimientofecha': 'F. Nac',
            'documentonumero': 'Número de Documento',
            'documentotipo': 'Tipo de Documento',
            'genero': 'Género',
            'direccion': 'Dirección',
            'obraSocial': 'Obra Social',
            'afiliado': 'Afiliado',
            'telefonocelular': 'Teléfono celular',
            'telefonofijo': 'Teléfono Fijo',
            'profesion': 'Profesión',
            'referente': 'Profesional Referente'
        }
        widgets = {
            'genero': forms.RadioSelect(),
            'nacimientofecha': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }
