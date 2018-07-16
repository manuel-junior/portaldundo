from django.contrib import admin
import datetime
from django.utils import timezone

from .models import Emprego, Endereco, Categoria


# class EmpregoAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['titulo']}),
#         ('Data informaçao', {'fields': ['pub_data'], 'classes': ['collapse']}),
#     ]
#     list_filter = ['pub_data']
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_data <= now
#
#     was_published_recently.admin_order_field = 'pub_data'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Publicado recentemente?'
#

# class EnderecoInLine(admin.StackedInline):
#     model = Endereco
#     raw_id_fields = ['job']
#     extra = 1
#
# class EmpregoAdmin(admin.ModelAdmin):
#     date_hierarchy = 'pub_data'
#     list_display = ['title', 'disponivel']
#     list_filter = ['pub_data', 'disponivel']
#     inlines = [EnderecoInLine]
#
# admin.site.register(Emprego, EmpregoAdmin)
# admin.site.register(Rua)
class EnderecoInline(admin.StackedInline):
    model = Emprego
    raw_id_fields = ['endereco']
    list_display = ['title', 'disponivel']
    extra = 1

class EmpregoAdmin(admin.ModelAdmin):
    inlines = [EnderecoInline]

admin.site.register(Endereco, EmpregoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}
admin.site.register(Categoria, CategoriaAdmin)