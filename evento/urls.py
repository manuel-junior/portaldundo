from django.urls import include, path

from . import views

app_name = 'evento'

urlpatterns = [
    path('', views.EventoListView.as_view(), name='evento'),
]