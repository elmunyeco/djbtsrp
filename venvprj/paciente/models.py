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

    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    nacimientoFecha = models.DateField(null=True)
    documentoNumero = models.CharField(max_length=20, null=True)
    documentoTipo = models.CharField(
        max_length=3, choices=DOCUMENTO_TIPO, default='DNI', null=True)
    genero = models.CharField(max_length=2, choices=GENERO, default='M')
    direccion = models.CharField(max_length=256, null=True)
    localidad = models.CharField(max_length=128, null=True)
    obraSocial = models.CharField(max_length=128, null=True)
    plan = models.CharField(max_length=128, null=True)
    afiliado = models.CharField(max_length=128, null=True)
    telefono1 = models.CharField(max_length=12, null=True)
    telefono2 = models.CharField(max_length=12, null=True)
    email = models.EmailField(max_length=128, null=True)
    profesion = models.CharField(max_length=128, null=True)
    referente = models.CharField(max_length=128, null=True)

    def __str__(self):
        return ("Paciente: %s" % self.nombre)

    class Meta:
        ordering = ['id']


class HistoriaClinica(models.Model):
    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    descripcion = models.TextField(null=True)


def create_hc(sender, instance, signal, **kwargs):
    HistoriaClinica.objects.create(paciente=instance, descripcion='Historia Clínica ({0}) de {1} {2}'.format(
        1, instance.nombre, instance.apellido))


post_save.connect(create_hc, sender=Paciente)
