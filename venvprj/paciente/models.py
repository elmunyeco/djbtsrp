from django.db.models.signals import post_save
from django.db import models

# Create your models here.


class Paciente(models.Model):
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    DOCUMENTO_TIPO = (
        ('DNI', 'Documento de Identidad'),
        ('CI', 'Cedula de Identidad'),
        ('LE', 'Libreta de Enrolamiento'),
        ('LC', 'Libreta Civica'),
    )

    nombre = models.CharField('Nombre', max_length=128)
    apellido = models.CharField('Apellido', max_length=128)
    nacimientofecha = models.DateField('Fecha de Nacimiento', null=True)
    documentotipo = models.CharField(
        'Tipo de Documento', max_length=3, choices=DOCUMENTO_TIPO, default='DNI', null=True)
    documentonumero = models.CharField(
        'Numero de Documento', max_length=20, null=True)
    genero = models.CharField(
        'Genero', max_length=2, choices=GENERO, default='M')
    direccion = models.CharField('Direccion', max_length=256, null=True)
    localidad = models.CharField('Localidad', max_length=128, null=True)
    obrasocial = models.CharField('Obra Social', max_length=128, null=True)
    plan = models.CharField('Plan', max_length=128, null=True)
    afiliado = models.CharField('Afiliado', max_length=128, null=True)
    telefonocelular = models.CharField('Telefono Celular', max_length=12, null=True)
    telefonofijo = models.CharField('Telefono Fijo', max_length=12, null=True)
    email = models.EmailField('Mail', max_length=128, null=True)
    profesion = models.CharField('Profesion', max_length=128, null=True)
    referente = models.CharField('Medico Referente', max_length=128, null=True)

    def __str__(self):
        return ("Paciente: %s %s" % self.nombre, self.apellido)

    class Meta:
        ordering = ['apellido', 'nombre']


class HistoriaClinica(models.Model):
    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    descripcion = models.TextField(null=True)


class Diagnosticos(models.Model):
    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    hipertensionarterial = models.BooleanField('Hipertension Arterial', default=False)
    diabetes1 = models.BooleanField('Diabetes Tipo I', default=False)
    diabetes2 = models.BooleanField('Diabetes Tipo 2', default=False)

def create_hc(sender, instance, signal, **kwargs):
    HistoriaClinica.objects.create(paciente=instance, descripcion='Historia Clínica ({0}) de {1} {2}'.format(
        1, instance.nombre, instance.apellido))

def create_diagnostico(sender, instance, signal, **kwargs):
    Diagnosticos.objects.create(paciente=instance)

post_save.connect(create_hc, sender=Paciente)
post_save.connect(create_diagnostico, sender=Paciente)