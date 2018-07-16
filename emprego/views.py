import json
from django.http import Http404, HttpResponse

from django.shortcuts import render, get_object_or_404
from .models import Emprego, Categoria
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import naturalday

def emprego(request, categoria_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    empregos = Emprego.objects.filter(disponivel=True, pub_data__lte=timezone.now()).order_by('-pub_data')[:5]
    template_name = "emprego.html"
    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        empregos = Emprego.objects.filter(categoria=categoria)

    return render(request, template_name, {'empregos': empregos,
                                           'categorias': categorias,
                                           'categoria':categoria,})

def ajax_detail(request, title, id):
    emprego = get_object_or_404(Emprego, id=id, title=title)

    if request.is_ajax():
        data = {
            'title': emprego.title,
            'empresa': emprego.empresa,
            'text':emprego.text,
            'imagem_url':json.dumps(str(emprego.image)),
            'endereco':json.dumps(str(emprego.endereco)),
            'date':naturalday(emprego.pub_data),
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
