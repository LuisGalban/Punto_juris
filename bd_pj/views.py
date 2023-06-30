from django.shortcuts import render, redirect
from .models import usuarios, solicitudes_de_investigacion, organismos, actos, gacetas_oficiales, PEPs, solicitudes_usuarios

# Create your views here.
def usuariosV(request):
    return render(request, 'usuarios.html')

def create_usuario(request):
    usuario = usuarios(nombre=request.POST['nombre'], 
        tipo_de_documento_identificatorio=request.POST['tipo_de_documento_identificatorio'],
        nr_documento_identidad=request.POST['nr_documento_identidad'],
        correo_electronico_afiliado=request.POST['correo_electronico_afiliado'],
        tipo_de_usuario=request.POST['tipo_de_usuario'],
        tipo_de_suscripcion=request.POST['tipo_de_suscripcion'],
        nr_de_usuarios=request.POST['nr_de_usuarios'],
        fecha_de_suscripcion=request.POST['fecha_de_suscripcion'],
        ultima_renovacion=request.POST['ultima_renovacion'],
        suscripcion_automatica=request.POST['suscripcion_automatica'],
        fecha_de_cancelacion=request.POST['fecha_de_cancelacion'],
        solicitudes_de_investigacion=request.POST['solicitudes_de_investigacion'],
        rol=request.POST['rol']
        )
    usuario.save()
    return redirect('../../usuarios/')

def usuariosR(request):
    users = usuarios.objects.all()
    relaciones = solicitudes_usuarios.objects.all()
    return render(request, 'usuarios_r.html', { "users": users , "relaciones" : relaciones})

def solicitudes(request):
    return render(request, 'solicitudes_de_investigacion.html')

def create_solicitud(request):
    solicitud = solicitudes_de_investigacion(asunto=request.POST['asunto'], 
        descripcion=request.POST['descripcion'],
        solicitante=request.POST['solicitante'],
        fecha_de_solicitud=request.POST['fecha_de_solicitud'],
        organismos_relacionados=request.POST['organismos_relacionados'],
        actos_relacionados=request.POST['actos_relacionados'],
        adjunto=request.POST['adjunto'],
        respuesta=request.POST['respuesta'],
        fecha_de_respuesta=request.POST['fecha_de_respuesta'],
        respuesta_aprobada=request.POST['respuesta_aprobada'],
        )
    solicitud.save()
    return redirect('../../solicitud/')

def organismosV(request):
    return render(request, 'organismos.html')

def create_organismo(request):
    organismo = organismos(organos=request.POST['organos'],
        solicitudes_de_investigacion=request.POST['solicitudes_de_investigacion'],
        ministerio_principal=request.POST['ministerio_principal'],
        subordinado_A=request.POST['subordinado_A'],
        cordinado_Por=request.POST['cordinado_Por'],
        acto_de_creacion=request.POST['acto_de_creacion'],
        nr_de_gaceta_creacion=request.POST['nr_de_gaceta_creacion'],
        acto_que_regula_su_organismo=request.POST['acto_que_regula_su_organismo'],
        nr_de_gaceta_acto_organizacion=request.POST['nr_de_gaceta_acto_organizacion'],
        encargado_actual=request.POST['encargado_actual'],
        acto_de_designacion=request.POST['acto_de_designacion'],
        nr_de_gaceta_acto_designacion=request.POST['nr_de_gaceta_acto_designacion'],
        notas=request.POST['notas'],
        actos_emitidos=request.POST['actos_emitidos'],
        funcion_publica=request.POST['funcion_publica'],
        territorialidad=request.POST['territorialidad'],
        telefono_contacto=request.POST['telefono_contacto'],
        correo_contacto=request.POST['correo_contacto'],
        ubicacion_oficinas=request.POST['ubicacion_oficinas'],
        fecha_designacion=request.POST['fecha_designacion']
        )
    organismo.save()
    return redirect('../../organismos/')

def actosV(request):
    return render(request, 'actos.html')

def create_acto(request):
    acto = actos(acto=request.POST['actos'],
        solicitudes_de_investigacion=request.POST['solicitudes_de_investigacion'],
        organos_creados=request.POST['organos_creados'],
        regula_los_organos=request.POST['regula_los_organos'],
        designa_A=request.POST['designa_A'],
        gaceta_de_origen=request.POST['gaceta_de_origen'],
        fecha=request.POST['fecha'],
        fecha_de_publicacion=request.POST['fecha_de_publicacion'],
        organo_emisor=request.POST['organo_emisor'],
        contenido_acto=request.POST['contenido_acto'],
        contenido=request.POST['contenido'],
        )
    acto.save()
    return redirect('../../actos/')

def gacetasV(request):
    return render(request, 'gacetas_oficiales.html')

def create_gaceta(request):
    gaceta = gacetas_oficiales(nombre=request.POST['nombre'],
        actos=request.POST['actos'],
        fecha_publicacion=request.POST['fecha_publicacion'],
        tipo_de_gaceta=request.POST['tipo_de_gaceta'],
        territorialidad=request.POST['territorialidad'],
        sumario=request.POST['sumario'],
        )
    gaceta.save()
    return redirect('../../gacetas/')

def PEPsV(request):
    return render(request, 'PEPs.html')

def create_pep(request):
    pep = PEPs(nombre=request.POST['nombre'],
        organismos=request.POST['organismos'],
        acto_de_designacion=request.POST['acto_de_designacion'],
        fecha_designacion=request.POST['fecha_designacion']
        )
    pep.save()
    return redirect('../../pep/')