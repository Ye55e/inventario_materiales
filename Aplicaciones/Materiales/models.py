from django.db import models

# Create your models here.
class Materiales (models.Model):
    id_mat= models.AutoField(primary_key=True)
    nom_mat = models.CharField(max_length=100)
    tipo_mat = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=20)
    foto_mat = models.FileField(upload_to='materiales', null=True, blank=True )
    prec_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    
class Suministradores (models.Model):
    id_sumi = models.AutoField(primary_key=True)
    nom_sumi = models.CharField(max_length=100)
    direcc_sumi = models.CharField(max_length=100)
    telf_sumi = models.CharField(max_length=10)
    email = models.EmailField()
    
class Ordenes (models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Aprobada', 'Aprobada'),
        ('Recibida', 'Recibida'),
    ]
    id_ord = models.AutoField(primary_key=True)
    fecha_ord = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')  
    total = models.DecimalField(max_digits=10, decimal_places=2)
    suministrador = models.ForeignKey(Suministradores, on_delete=models.CASCADE,related_name='proveedores', null=True, blank=True )
    
class Existencias (models.Model):
    TIPOS_MOVIMIENTO = [
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida'),
    ]
    id_exis = models.AutoField(primary_key=True)
    cant_disp = models.PositiveIntegerField()
    tipo_mov = models.CharField(max_length=20, choices=TIPOS_MOVIMIENTO, default='Entrada')  
    fech_exis = models.DateField()
    material = models.ForeignKey(Materiales, on_delete=models.CASCADE,related_name='existencias', null=True, blank=True )
    orden = models.ForeignKey(Ordenes, on_delete=models.CASCADE,related_name='ordenes', null=True, blank=True )
    
    
    