from django.shortcuts import render, redirect
from .forms import PacienteForm 

# Create your views here.

def paciente_list(request):
    return render(request,'pt_crud/paciente_list.html')

def paciente_form(request):
    if request.method == "GET":
        form = PacienteForm()
        return render(request,'pt_crud/paciente_form.html',{'form':form})
    else:
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/paciente/list")


def paciente_del(request):
    return