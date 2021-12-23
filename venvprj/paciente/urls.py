from django.urls import path, include
from . import views
from .views import (PacienteListView, PacienteJSONListView,
                    PacienteDatatableListView, PacienteDetailView)
from django.conf.urls import url


app_name = 'paciente'

urlpatterns = [
    path('', views.index),
    path('lista/', views.PacienteDatatableListView.as_view(),
         name="ajax_paciente_list"),
    #    path('', views.PacienteListView.as_view(), name='paciente_list'),
    #    path('j/', views.PacienteJSONListView.as_view(), name='paciente_list_j'),
    path('create/', views.paciente_form, name='paciente_create'),
    path('<int:pk>/', views.PacienteDetailView.as_view(), name='paciente_detail'),
]
