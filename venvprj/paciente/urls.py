from django.urls import path, include
from . import views
from .views import (PacienteListView, PacienteDetailView)
from django.conf.urls import url


app_name='paciente'

urlpatterns = [
    #path('', views.paciente_form),  # localhost:p/ptid OJO CUIDADO
    #path('list', views.PacienteListView.as_view(), name='pacientes')
    url(r'^$', views.PacienteListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', PacienteDetailView.as_view, name='detail')
]
