from django.shortcuts import render, redirect
from .forms import PacienteForm 
from .models import Paciente

# Create your views here.

def paciente_list(request):
    context = {'paciente_list':Paciente.objects.all()}
    return render(request,'pt_crud/paciente_list.html',context)

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