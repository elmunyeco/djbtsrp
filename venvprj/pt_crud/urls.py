from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.paciente_form),  # localhost:p/ptid
    #path('list', views.paciente_list)
    path('list', views.PacienteListView.as_view(), name='pacientes')
]
