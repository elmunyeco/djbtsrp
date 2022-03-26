from django.urls import path, include
from .  import views
from .views import (PacienteListView, PacienteJSONListView,
                    PacienteDatatableListView, PacienteDetailView)
from django.conf.urls import url


app_name = 'paciente'

""" urlpatterns = [
    path('', views.index),
    path('lista/', views.PacienteDatatableListView.as_view(),
         name="ajax_paciente_list"),
    #    path('', views.PacienteListView.as_view(), name='paciente_list'),
    #    path('j/', views.PacienteJSONListView.as_view(), name='paciente_list_j'),
    path('create/', views.paciente_form, name='create_paciente_form'),
    path('create/POST', views.paciente_form, name='create_paciente_form'),
    path('update/<int:pk>/', views.paciente_form, name='update_paciente_form'),
] """


urlpatterns = [
    path('', views.index),
    path('lista/', views.PacienteDatatableListView.as_view(),
         name="ajax_paciente_list"),
    #    path('', views.PacienteListView.as_view(), name='paciente_list'),
    #    path('j/', views.PacienteJSONListView.as_view(), name='paciente_list_j'),
    url(r'^create/', views.paciente_form, name='create_paciente_form'),
    url(r'^update/(?P<id>\d+)/$', views.paciente_update, name='update_paciente_form'),
]

#handler404 = "paciente.views.page_not_found"
