from django.db import models
from datetime import datetime

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']
        db_table = 'tipo'

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']
        db_table = 'categoria'

class Employee(models.Model):
    #Relacionar Tablas
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    categ = models.ManyToManyField(Category)

    names = models.CharField(max_length=150, verbose_name='Nombres')
    last_name = models.CharField(max_length=150, verbose_name='Apellidos')
    dui = models.CharField(max_length=10, verbose_name='DUI', unique=True)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    date_creation = models.DateTimeField(auto_now=True, verbose_name='Fecha de Creación')
    date_update = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualización')
    age = models.PositiveIntegerField(default=0, verbose_name='Edad')
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Salario')
    state = models.BooleanField(default=True, verbose_name='Estado')
    gender = models.CharField(max_length=50, verbose_name='Sexo')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
