from django.contrib import admin

from .models import Hospedagem, Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}
admin.site.register(Categoria, CategoriaAdmin)


class HospedagemAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'categoria', 'telefone', 'alt_telefone', 'email','endereco','criado',]
    list_filter = ['criado', 'categoria']
    prepopulated_fields = {'slug': ('nome',)}
admin.site.register(Hospedagem, HospedagemAdmin)
