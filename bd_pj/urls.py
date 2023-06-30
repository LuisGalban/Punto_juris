from django.urls import path
from .views import *
#forms/usuarios/forms/usuarios/new_user/
urlpatterns = [
    path('usuarios_r/', usuariosR),
    path('usuarios/',usuariosV),
    path('usuarios/new_user/', create_usuario),
    path('solicitud/',solicitudes),
    path('solicitud/new_solicitud/',create_solicitud),
    path('organismos/', organismosV),
    path('organismos/new_organismo/', create_organismo),
    path('actos/', actosV),
    path('actos/new_acto/', create_acto),
    path('gacetas/', gacetasV),
    path('gacetas/new_gaceta/', create_gaceta),
    path('pep/', PEPsV),
    path('pep/new_PEP/', create_pep)
]