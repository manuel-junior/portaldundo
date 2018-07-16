from django.utils import timezone
from django.views.generic import ListView

from .models import Evento


class EventoListView(ListView):
    model = Evento
    template_name = "evento.html"
    context_object_name = 'ultimos_eventos'
    eventos = Evento.objects.all().order_by('-start_dia') #Ira ordenar os eventos pela data de inicio (Decrescente)
    evento = None

    if eventos is not None:
        for e in eventos:
            if e.today() or e.happening() or e.future():
                evento = e

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['evento'] = self.evento
        return context



    # def get_queryset(self):
    #     """
    #     Return the last five published event (not including those set to be
    #     published in the future).
    #     """
    #     return Evento.objects.filter(
    #         pub_data__lte=timezone.now()
    #     ).order_by('-pub_data')[:5]
