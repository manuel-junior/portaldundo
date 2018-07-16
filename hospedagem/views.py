from django.shortcuts import render, get_object_or_404
from .models import Hospedagem, Categoria


def hospedagem(request):
    categoria = None
    hospedarias = None
    hoteis = None
    template_name = "hospedagem.html"

    #c_hospedaria = get_object_or_404(Categoria, slug="hospedaria")
    #c_hotel = get_object_or_404(Categoria, slug="hotel")

    #hospedarias = Hospedagem.objects.filter(categoria=c_hospedaria)

    #hoteis = Hospedagem.objects.filter(categoria=c_hotel)

    #c = {
    #    'hospedarias': hospedarias,
    #    'hoteis': hoteis,
    #}
    categorias = Categoria.objects.all()

    for c in categorias:
        if c.nome =="Hospedaria":
            categoria = get_object_or_404(Categoria, slug="hospedaria")
            hospedarias = Hospedagem.objects.filter(categoria=categoria)
        elif c.nome =="Hotel":
            categoria = get_object_or_404(Categoria, slug="hotel")
            hoteis = Hospedagem.objects.filter(categoria=categoria)

    # if categoria:
    #     if categoria == "hotel":
    #         categoria = get_object_or_404(Categoria, slug=categoria)
    #         hospedarias = Hospedagem.objects.filter(categoria=categoria)
    #         print("Categoria %s", categoria.nome)
    #
    #     elif categoria == "hospedaria":
    #         categoria = get_object_or_404(Categoria, slug=categoria)
    #         hoteis = Hospedagem.objects.filter(categoria=categoria)
    #         print("Categoria %s", categoria.nome)

    return render(request, template_name, {'hospedarias': hospedarias,
                                            'hoteis': hoteis,
                                            'categorias':categorias,
                                            'categoria':categoria,
                                           })
