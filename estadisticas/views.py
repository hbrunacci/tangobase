from django.shortcuts import render
from .forms import EventForm
from .models import *
from django.views.generic import TemplateView,DetailView,DeleteView,CreateView,ListView


class Listado(ListView):
    model = Evento
    template_name = 'estadisticas/eventos_list.html'

class Crear(CreateView):
    model = Evento
    template_name = 'estadisticas/new_event.html'
    fields = ('paciente',)

def event_new(request):
    form = EventForm
    return render(request, 'estadisticas/new_event.html', {'form': form})
