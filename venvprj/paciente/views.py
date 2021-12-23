from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PacienteForm
from .models import Paciente
from .mixins import SearchPacientesMixin, SearchPacientesJSONMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from ajax_datatable.views import AjaxDatatableView


def index(request):
    return render(request, 'paciente/index.html', {})


def paciente_form(request):
    if request.method == "GET":
        form = PacienteForm()
        return render(request, 'paciente/paciente_form.html', {'form': form})
    else:
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/paciente/list")


def paciente_del(request):
    return


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

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False, },
        {'name': 'nombre', 'visible': True, },
    ]
