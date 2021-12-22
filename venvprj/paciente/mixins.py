from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse


class SearchPacientesMixin:

    def get_queryset(self):
        queryset = super(SearchPacientesMixin, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            return queryset.filter(
                Q(nombre__icontains=search) |
                Q(apellido__icontains=search) |
                Q(documentonumero__icontains=search)
            )
        return queryset


class SearchPacientesJSONMixin:

    def get_queryset(self):
        queryset = super(SearchPacientesJSONMixin, self).get_queryset()
        search = self.request.GET.get('search')
        print(self.request.GET)
        if search:
            return queryset.filter(
                Q(nombre__icontains=search) |
                Q(apellido__icontains=search) |
                Q(documentonumero__icontains=search)
            )
        return queryset.values_list("id", "nombre", "apellido", "documentonumero")

    def get(self, request, *args, **kwargs):
        caca = list(self.get_queryset())
        return JsonResponse({'pija': caca}, safe=False)
