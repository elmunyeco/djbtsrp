from django.shortcuts import render, redirect
from .forms import PatientForm 

# Create your views here.

def patient_list(request):
    return render(request,'pt_crud/patient_list.html')

def patient_form(request):
    if request.method == "GET":
        form = PatientForm()
        return render(request,'pt_crud/patient_form.html',{'form':form})
    else:
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/patient/list")


def patient_del(request):
    return