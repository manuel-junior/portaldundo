from django import template
from django.db.models import Count

register = template.Library()

from ..models import Noticia

@register.simple_tag
def total_noticias():
	return Noticia.published.count()

@register.inclusion_tag('latest_noticias.html')
def show_latest_noticias(count=5):
	latest_noticias = Noticia.published.order_by('-publish')[:count]
	return {'latest_noticias': latest_noticias}


@register.inclusion_tag('comunidade/noticias/ultimas_noticias.html')
def mostrar_ultimas_noticias(count=4):
	ultimas_noticias = Noticia.published.order_by('-categoria_noticia', '-publish')[:count]
	return {'ultimas_noticias': ultimas_noticias}