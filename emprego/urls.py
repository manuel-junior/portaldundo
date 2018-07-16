from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'emprego'

urlpatterns = [
    path('', views.emprego, name='emprego'),
    path('<categoria_slug>/', views.emprego, name='list_by_categoria'),
    path('ajax/<title>/<id>/', views.ajax_detail, name='ajax_detail'),
]