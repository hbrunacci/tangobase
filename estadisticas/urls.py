from django.urls import path
from django.views.generic import TemplateView,CreateView
from .views import Crear,event_new,Listado

urlpatterns = [
    path('', TemplateView.as_view(template_name='estadisticas/estadisticas_base.html'), name='Home'),
    path('listar/', Listado.as_view(), name='Lista'),
    path('nuevo/', Crear.as_view(), name='nuevo'),
    path('post_new/', event_new, name='event_new'),
]