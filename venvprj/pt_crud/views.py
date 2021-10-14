from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import PacienteForm 
from .models import Paciente

# Create your views here.

def paciente_list(request):
    pacientes = Paciente.objects.all()
    paginator = Paginator(pacientes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'paciente_list':pacientes}
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