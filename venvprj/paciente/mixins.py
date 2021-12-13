from django.db.models import Q


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
