from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PacienteForm
from .models import Paciente
from .mixins import SearchPacientesMixin

from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


""" def paciente_list(request):
    pacientes_list = Paciente.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(pacientes_list, 10)
    page_obj = paginator.get_page(page)
    page_range = paginator.get_elided_page_range(number=page)

    try:
        pacientes = paginator.page(page)
    except PageNotAnInteger:
        pacientes = paginator.page(1)
    except EmptyPage:
        pacientes = paginator.page(paginator.num_pages, on_each_side=3)

    context = {'paciente_list': pacientes}
    return render(request, 'paciente/paciente_list.html', context)
 """


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


""" 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

 """


class PacienteDetailView(DetailView):

    model = Paciente
