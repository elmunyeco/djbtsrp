from django.urls import path, include
from . import views
from .views import (PacienteListView, PacienteDetailView)
from django.conf.urls import url


app_name = 'paciente'

urlpatterns = [
    path('', views.PacienteListView.as_view(), name='paciente_list'),
    path('create/', views.paciente_form, name='paciente_create'),
    path('<int:pk>/', views.PacienteDetailView.as_view(), name='paciente_detail'),

#    path('<int:pk>/update/', v.expense_update, name='expense_update'),
#    path('<int:pk>/delete/', v.expense_delete, name='expense_delete'),
]
