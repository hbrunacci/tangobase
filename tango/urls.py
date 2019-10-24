"""tango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from estadisticas.views import *

transfusiones_crud = transfusionesCRUD()
ecp_crud = ecpCRUD()
medicacion_habitual_crud = medicacion_habitualCRUD()
clinica_crud = clinicaCRUD()
procedimiento_crud = procedimientoCRUD()
opciones_viabilidad_crud = opciones_viabilidadCRUD()
opciones_metodo_crud = opciones_metodoCRUD()
resultados_seguimiento_crud = resultados_seguimientoCRUD()
estudio_crud = estudioCRUD()
cirujanos_crud = cirujanosCRUD()
ayudantes_crud = ayudantesCRUD()
evento_crud = eventoCRUD()
antecedentes_crud = antecedentesCRUD()
cirugia_crud = cirugiaCRUD()
complicaciones_crud = complicacionesCRUD()
ecodoppler_crud = ecodopplerCRUD()
viablilidad_crud = viablilidadCRUD()
laboratorio_crud = laboratorioCRUD()
paciente_crud = pacienteCRUD()
alta_crud = altaCRUD()
seguimiento_crud = seguimientoCRUD()





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estadisticas.urls')),
    path('', include(transfusiones_crud.get_urls())),
    path('', include(ecp_crud.get_urls())),
    path('', include(medicacion_habitual_crud.get_urls())),
    path('', include(clinica_crud.get_urls())),
    path('', include(procedimiento_crud.get_urls())),
    path('', include(opciones_viabilidad_crud.get_urls())),
    path('', include(opciones_metodo_crud.get_urls())),
    path('', include(resultados_seguimiento_crud.get_urls())),
    path('', include(estudio_crud.get_urls())),
    path('', include(cirujanos_crud.get_urls())),
    path('', include(ayudantes_crud.get_urls())),
    path('', include(evento_crud.get_urls())),
    path('', include(antecedentes_crud.get_urls())),
    path('', include(cirugia_crud.get_urls())),
    path('', include(complicaciones_crud.get_urls())),
    path('', include(ecodoppler_crud.get_urls())),
    path('', include(viablilidad_crud.get_urls())),
    path('', include(laboratorio_crud.get_urls())),
    path('', include(alta_crud.get_urls())),
    path('', include(seguimiento_crud.get_urls())),
    path('', include(paciente_crud.get_urls())),
]
