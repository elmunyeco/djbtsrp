from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.patient_form),
    path('list/', include(views.patient_list))
]