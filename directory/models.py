from django.db import models
from spravchnik.models import Category, Region, District, Brand, Manufacturer, Country_origin, Position, Sensortype


class Organization(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    level = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200)
    latitude = models.CharField(max_length=100)
    longitude = models.IntegerField()

    class Meta:
        verbose_name_plural = "Organizations"
        verbose_name = "Organization"

    def __str__(self):
        return self.name


class Drone(models.Model):
    drone_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    country_origin = models.ForeignKey(Country_origin, on_delete=models.SET_NULL, null=True)
    production_year = models.IntegerField()
    mood = models.CharField(max_length=200)
    owner = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    operator = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = "Organizations"
        verbose_name = "Drone"

    def __str__(self):
        return self.name


class Employee(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    birthday = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=100)
    pasport_data = models.IntegerField()

    class Meta:
        verbose_name_plural = "Employees"
        verbose_name = "Employee"

    def __str__(self) -> str:
        return self.name


class Sensor(models.Model):
    sensor_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Sensortype, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    country_origin = models.ForeignKey(Country_origin, on_delete=models.SET_NULL, null=True)
    production_year = models.IntegerField()
    condition = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    type_host = models.CharField(max_length=100)
    host_id = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Sensors"
        verbose_name = "Sensor"

    def __str__(self) -> str:
        return self.name


class Object(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    level = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.IntegerField()

    class Meta:
        verbose_name_plural = "Objects"
        verbose_name = "Object"

    def __str__(self) -> str:
        return self.name
