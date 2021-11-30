from django.db import models

class Bus(models.Model):
    licence_plate = models.CharField('Patente', max_length=6)
    year = models.IntegerField('Año')
    brand = models.CharField('Marca', max_length=30)
    model = models.CharField('Modelo', max_length=20)
    in_service = models.BooleanField('En Servicio')

    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'


class Driver(models.Model):
    first_name = models.CharField('Nombre', max_length=60)
    fathers_last_name = models.CharField('Apellido Paterno', max_length=30)
    mothers_last_name = models.CharField('Apellido Materno', max_length=30)
    age = models.IntegerField('Edad')
    active = models.BooleanField('Chofer Activo')

    class Meta:
        verbose_name = 'Chofer'
        verbose_name_plural = 'Choferes'


class Route(models.Model):
    origin = models.CharField('Origen', max_length=50)
    destiny = models.CharField('Destino', max_length=50)
    active = models.BooleanField('Ruta Activa')

    class Meta:
        verbose_name = 'Trayecto'
        verbose_name_plural = 'Trayectos'


class Passenger(models.Model):
    first_name = models.CharField('Nombre', max_length=60)
    fathers_last_name = models.CharField('Apellido Paterno', max_length=30)
    mothers_last_name = models.CharField('Apellido Materno', max_length=30)

    class Meta:
        verbose_name = 'Pasajero'
        verbose_name_plural = 'Pasajeros'


class Trip(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    passengers = models.ManyToManyField(Passenger)

    class Meta:
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'
