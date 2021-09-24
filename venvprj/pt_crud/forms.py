from django import forms
from .models import Paciente


class PatientForm(forms.ModelForm):

    class Meta:
        model = Paciente
        #fields = ("",)
        fields = '__all__'
