from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.patient_form), #localhost:p/ptid
    path('list/', views.patient_list)
]