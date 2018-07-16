from django.urls import path

from . import views

app_name = 'hospedagem'

urlpatterns = [
    path('', views.hospedagem, name='hospedagem'),
]