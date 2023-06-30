from django.db import models
# Create your models here.

class usuarios(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    tipo_de_usuario = models.CharField(null=False,blank=False ,max_length=200)
    tipo_de_suscripcion = models.CharField(null=False, blank=False, max_length=15)
    nr_de_usuarios = models.IntegerField(null=False, blank=False)
    fecha_de_suscripcion = models.DateField(null=False, blank=False)
    ultima_renovacion = models.DateField(null=False, blank=False)
    suscripcion_automatica = models.BooleanField(null=False, blank=False)
    fecha_de_cancelacion = models.TextField(max_length=75,null=False, blank=False)
    tipo_de_documento_identificatorio = models.CharField(max_length=200, null=True, blank=True)
    nr_documento_identidad = models.IntegerField(null=True, blank=True)
    correo_electronico_afiliado = models.EmailField(max_length=200,null=False, blank=False)     
    solicitudes_de_investigacion = models.CharField(max_length=200, null=True, blank=True)
    rol = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural="usuarios"
  
class solicitudes_de_investigacion(models.Model):
    asunto = models.CharField(max_length=50, null=False,blank=False)
    descripcion = models.TextField(max_length=500,null=False,blank=False)
    solicitante = models.TextField(max_length=50,null=False,blank=False)
    organismos_relacionados = models.CharField(max_length=200, null=True, blank=True)
    actos_relacionados = models.CharField(max_length=200, null=True, blank=True)
    adjunto = models.FileField(null=True, blank=True)
    fecha_de_solicitud = models.DateField(null=False,blank=False)
    respuesta = models.TextField(null=True, blank=True)
    respuesta_aprobada = models.BooleanField(null=True, blank=True)
    fecha_de_respuesta = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.asunto
    
    class Meta:
        verbose_name_plural="Solicitudes de investigacion"
    
class organismos(models.Model):
    organos = models.CharField(max_length=200, null=False, blank=False)
    solicitudes_de_investigacion = models.CharField(max_length=50, null=True, blank=True)
    ministerio_principal = models.CharField(max_length=50, null=True, blank=True)
    subordinado_A = models.CharField(max_length=50, null=True, blank=True)
    cordinado_Por = models.CharField(max_length=50, null=True, blank=True)
    acto_de_creacion = models.CharField(max_length=200, null=True, blank=True)
    nr_de_gaceta_creacion = models.IntegerField(null=True, blank=True)
    acto_que_regula_su_organismo = models.TextField(null=True, blank=True)
    nr_de_gaceta_acto_organizacion = models.IntegerField(null=True, blank=True)
    encargado_actual = models.CharField(max_length=200, null=False, blank=False)
    acto_de_designacion = models.CharField(max_length=500,null=False, blank=False)
    nr_de_gaceta_acto_designacion = models.IntegerField(null=False, blank=False)
    notas = models.TextField(null=True, blank=True)
    actos_emitidos = models.TextField(null=True, blank=True)
    funcion_publica = models.CharField(max_length=50, null=False, blank=False)
    territorialidad = models.CharField(max_length=50, null=False, blank=False)
    telefono_contacto = models.CharField(max_length=20,null=True, blank=True)
    correo_contacto = models.EmailField(null=True, blank=True)
    ubicacion_oficinas = models.TextField(null=True, blank=True)
    fecha_designacion = models.DateField(null=False, blank=False)
    
    def __str__(self):
        return self.organos
    
    class Meta:
        verbose_name_plural="Organismos"
    
class actos(models.Model):
    acto = models.CharField(max_length=200, null=False, blank=False)
    solicitudes_de_investigacion = models.CharField(max_length=50, null=True, blank=True)
    organos_creados = models.CharField(max_length=500, null=True, blank=True)
    regula_los_organos = models.CharField(max_length=500, null=True, blank=True)
    designa_A = models.CharField(max_length=500, null=True, blank=True)
    gaceta_de_origen = models.IntegerField(null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    fecha_de_publicacion = models.DateField(null=False, blank=False)
    organo_emisor = models.CharField(max_length=200, null=True, blank=True)
    contenido_acto = models.TextField(null=True, blank=True)
    contenido = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.acto
    
    class Meta:
        verbose_name_plural="Actos"

class gacetas_oficiales(models.Model):
    nombre = models.CharField(max_length=20, null=False, blank=False)
    actos = models.CharField(max_length=200)
    fecha_publicacion = models.DateField(null=False, blank=False)
    tipo_de_gaceta = models.CharField(max_length=500)
    territorialidad = models.CharField(max_length=500)
    sumario = models.TextField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural="Gacetas Oficiales"

class PEPs(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    organismos = models.CharField(max_length=200, null=False, blank=False)
    acto_de_designacion = models.CharField(max_length=500,null=False, blank=False)
    fecha_designacion = models.DateField(null=False, blank=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural="PEPs"
    
 
#Relacion Solicitudes - Usuarios
class solicitudes_usuarios(models.Model):
    id_solicitudes = models.ForeignKey(solicitudes_de_investigacion, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name_plural="Solicitudes/Usuarios"

#Relacion Solicitudes - Organismos
class solicitudes_organismos(models.Model):
    id_solicitudes = models.ForeignKey(solicitudes_de_investigacion, on_delete=models.CASCADE)
    id_organismos = models.ForeignKey(organismos, on_delete=models.CASCADE)
    
#Relacion Solicitudes - Actos  
class solicitudes_actos(models.Model):
    id_solicitudes = models.ForeignKey(solicitudes_de_investigacion, on_delete=models.CASCADE)
    id_actos = models.ForeignKey(actos, on_delete=models.CASCADE)
    
#Relacion: Organismo - Actas - Peps
class organismos_peps_actas(models.Model):
    id_organismos = models.ForeignKey(organismos, on_delete=models.CASCADE)
    id_peps = models.ForeignKey(PEPs, on_delete=models.CASCADE)
    id_actos = models.ForeignKey(actos, on_delete=models.CASCADE)

#Relacion: Organismo - PEPs
class organismos_peps(models.Model):
    id_organismos = models.ForeignKey(organismos, on_delete=models.CASCADE)
    id_peps = models.ForeignKey(PEPs, on_delete=models.CASCADE)
    
#Relacion: Organismos - Actos
class organismos_actos(models.Model):
    id_organismos = models.ForeignKey(organismos, on_delete=models.CASCADE)
    id_actos = models.ForeignKey(actos, on_delete=models.CASCADE)
    
#Relacion: Gacetas - Actos
class gacetas_actos(models.Model):
    id_gacetas = models.ForeignKey(gacetas_oficiales, on_delete=models.CASCADE)
    id_actos = models.ForeignKey(actos, on_delete=models.CASCADE)