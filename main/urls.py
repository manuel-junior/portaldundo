from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('restaurante/', views.RestauranteView.as_view(), name='restaurante'),
    path('servicos/', views.ServicoView.as_view(), name='servico'),
    path('noticia/', views.NoticiaView.as_view(), name='noticia'),
    path('historia/', views.SobreView.as_view(), name='sobre_dundo'),
    path('patrimonio/', views.PatrimonioView.as_view(), name='patrimonio'),
    path('contacto/', views.contacto, name='contacto'),
]