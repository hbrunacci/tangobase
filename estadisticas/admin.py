from django.contrib import admin
from .models import *


class Evento_Admin(admin.ModelAdmin):
    pass


class Antecedentes_Admin(admin.ModelAdmin):
    pass


class Cirugia_Admin(admin.ModelAdmin):
    pass


class Complicaciones_Admin(admin.ModelAdmin):
    pass


class Ecodoppler_Admin(admin.ModelAdmin):
    pass


class Viablilidad_Admin(admin.ModelAdmin):
    pass


class Laboratorio_Admin(admin.ModelAdmin):
    pass


class Alta_Admin(admin.ModelAdmin):
    pass


class Seguimiento_Admin(admin.ModelAdmin):
    pass


admin.site.register(Transfusiones)
admin.site.register(ECP)
admin.site.register(Medicacion_Habitual)
admin.site.register(Clinica)
admin.site.register(Procedimiento)
admin.site.register(Opciones_viabilidad)
admin.site.register(Opciones_metodo)
admin.site.register(Resultados_seguimiento)
admin.site.register(Estudio)
admin.site.register(Cirujanos)
admin.site.register(Ayudantes)
admin.site.register(Evento)
admin.site.register(Antecedentes)
admin.site.register(Cirugia)
admin.site.register(Complicaciones)
admin.site.register(Ecodoppler)
admin.site.register(Viablilidad)
admin.site.register(Laboratorio)
admin.site.register(Alta)
admin.site.register(Seguimiento)
admin.site.register(Paciente)


