from django.http import Http404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PacienteForm
from .models import Paciente
from .mixins import SearchPacientesMixin, SearchPacientesJSONMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from ajax_datatable.views import AjaxDatatableView

from django.http import Http404


def index(request):
    return render(request, 'paciente/index.html', {})


def paciente_form(request):
    if request.method == "GET":
        print("PACIENTE CREATE FORM: EN EL GET")
        p_form = PacienteForm()
        return render(request, 'paciente/paciente_form.html', {'p_form': p_form})
    else:
        p_form = PacienteForm(request.POST)
        print("EN EL POST")
        if p_form.is_valid():
            p_form.save()
            return redirect("/pacientes/")


def paciente_update(request, id):
    try:
        print("PACIENTE UPDATE FORM: EN EL GET")
        p_form = PacienteForm()
        print(id)
        paciente = Paciente.objects.get(id=id)
        p_form = PacienteForm(instance=paciente)
        return render(request, 'paciente/paciente_form.html', {'p_form': p_form})
    except Paciente.DoesNotExist:
        return render(request, 'paciente/404.html', status=404)

def paciente_del(request):
    return


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


class PacienteListView(SearchPacientesMixin, ListView):
    model = Paciente
    paginate_by = 10


class PacienteJSONListView(SearchPacientesJSONMixin, ListView):
    model = Paciente
    paginate_by = 10


class PacienteDetailView(DetailView):
    model = Paciente


class PacienteDatatableListView(AjaxDatatableView):
    model = Paciente
    title = 'Pacientes'
    initial_order = [["nombre", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'
    show_column_filters = False

    column_defs = [

        {'name': 'id', 'visible': False, 'searchable': True},
        {'name': 'nombre', 'visible': True},
        {'name': 'apellido', 'visible': True},
        {'name': 'documentonumero', 'visible': True},

    ]
