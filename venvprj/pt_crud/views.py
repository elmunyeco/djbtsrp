from django.shortcuts import render
from .forms import PatientForm 

# Create your views here.

def patient_list(request):
    return render(request,'pt_crud/patient_list.html')

def patient_form(request):
    form = PatientForm()
    return render(request,'pt_crud/patient_form.html',{'form':form})

def patient_del(request):
    return