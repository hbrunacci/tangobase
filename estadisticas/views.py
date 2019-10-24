from __future__ import unicode_literals
from django.contrib import admin
from .models import *
from django.utils.translation import ugettext_lazy as _

from cruds_adminlte.crud import CRUDView
from cruds_adminlte.inline_crud import InlineAjaxCRUD
from cruds_adminlte.filter import FormFilter

from django.views.generic.base import TemplateView
from django import forms

class transfusionesCRUD(CRUDView):
    model = Transfusiones
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class ecpCRUD(CRUDView):
    model = ECP
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class medicacion_habitualCRUD(CRUDView):
    model = Medicacion_Habitual
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class clinicaCRUD(CRUDView):
    model = Clinica
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class procedimientoCRUD(CRUDView):
    model = Procedimiento
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class opciones_viabilidadCRUD(CRUDView):
    model = Opciones_viabilidad
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class opciones_metodoCRUD(CRUDView):
    model = Opciones_metodo
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class resultados_seguimientoCRUD(CRUDView):
    model = Resultados_seguimiento
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class estudioCRUD(CRUDView):
    model = Estudio
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class cirujanosCRUD(CRUDView):
    model = Cirujanos
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class ayudantesCRUD(CRUDView):
    model = Ayudantes
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class eventoCRUD(CRUDView):
    model = Evento
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class antecedentesCRUD(CRUDView):
    model = Antecedentes
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class cirugiaCRUD(CRUDView):
    model = Cirugia
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class complicacionesCRUD(CRUDView):
    model = Complicaciones
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class ecodopplerCRUD(CRUDView):
    model = Ecodoppler
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class viablilidadCRUD(CRUDView):
    model = Viablilidad
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class laboratorioCRUD(CRUDView):
    model = Laboratorio
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class altaCRUD(CRUDView):
    model = Alta
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class seguimientoCRUD(CRUDView):
    model = Seguimiento
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
class pacienteCRUD(CRUDView):
    model = Paciente
    views_avaible = ['create', 'list', 'delete', 'update', 'detail']
    
