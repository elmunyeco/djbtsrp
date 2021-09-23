from django.shortcuts import render

# Create your views here.

def patient_list(request):
    return render(request,'pt_crud/patient_list.html')

def patient_form(request):
    return render(request,'pt_crud/patient_form.html')

def patient_del(request):
    return