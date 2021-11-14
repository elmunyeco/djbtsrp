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

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.model = models.Model.object.create(descripcion='culoroto')
            super().save(*args, **kwargs)

    class Meta:
        ordering = ['id']


class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(
        Paciente, default=None, on_delete=models.CASCADE)
    """ descripcion = models.TextField(null=True) """
    """
        paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    """

    class Meta:
        ordering = ['id']
