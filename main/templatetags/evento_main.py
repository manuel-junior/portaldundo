from django import template

from evento.models import Evento

register = template.Library()


@register.inclusion_tag('events_main.html')
def show_events(count=5):
    active_events_ids = []

    if Evento is not None:
        for event in Evento.objects.all():
            if event.future() or event.happening() or event.today():
                active_events_ids.append(event.id)

    events = Evento.objects.filter(id__in=active_events_ids).order_by('start_dia')[:count]

    return {'events': events}
