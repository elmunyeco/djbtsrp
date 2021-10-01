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
         ('LE', 'Libreta da Enrolamiento'),
         ('LC', 'Libreta Civica'),
     )

     id = models.UUIDField(
         primary_key=True, default='uuid.uuid4', editable=False)
     nombre = models.CharField(max_length=128)
     apellido = models.CharField(max_length=128)
     nacimiento_fecha = models.DateField(null=True)
     documento_numero = models.CharField(max_length=20, null=True)
     documento_tipo = models.CharField(
         max_length=3, choices=DOCUMENTO_TIPO, default='DNI')
     genero = models.CharField(max_length=2, choices=GENERO, default='M')
     direccion = models.CharField(max_length=256, null=True)
     localidad = models.CharField(max_length=128, null=True)
     obra_social = models.CharField(max_length=128, null=True)
     plan = models.CharField(max_length=128, null=True)
     afiliado = models.CharField(max_length=128, null=True)
     telefono_1 = models.CharField(max_length=12, null=True)
     telefono_2 = models.CharField(max_length=12, null=True)
     email = models.EmailField(max_length=128, null=True)
     profesion = models.CharField(max_length=128, null=True)
     referente = models.CharField(max_length=128, null=True)
