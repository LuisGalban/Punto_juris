from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(usuarios)
admin.site.register(solicitudes_de_investigacion)
admin.site.register(organismos)
admin.site.register(actos)
admin.site.register(gacetas_oficiales)
admin.site.register(PEPs)
admin.site.register(solicitudes_usuarios)