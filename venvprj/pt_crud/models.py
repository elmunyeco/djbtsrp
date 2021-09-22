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
     nacimiento_fecha = models.DateField()
     documento_numero = models.CharField(max_length=20)
     documento_tipo = models.CharField(
         max_length=3, choices=DOCUMENTO_TIPO, default='DNI')
     genero = models.CharField(max_length=2, choices=GENERO, default='M')
     direccion = models.CharField(max_length=256)
     localidad = models.CharField(max_length=128)
     obra_social = models.CharField(max_length=128)
     plan = models.CharField(max_length=128)
     afiliado = models.CharField(max_length=128)
     telefono_linea = models.CharField(max_length=12)
     telefono_celular = models.CharField(max_length=12)
     email = models.EmailField(max_length=128)
     profesion = models.CharField(max_length=128)
     referente = models.CharField(max_length=128)
