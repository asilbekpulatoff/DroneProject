from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Brands"
        verbose_name = "Brand"


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


class Country_origin(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"
        verbose_name = "Country"


class Manufacturer(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Manufacturers"
        verbose_name = "Manufacturer"    


class Position(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Positions"
        verbose_name = "Position"


class Region(models.Model):
    region_code = models.CharField(max_length=30)
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Regions"
        verbose_name = "Region"


class District(models.Model):
    district_code = models.CharField(max_length=155)
    name = models.CharField(max_length=155)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="districts")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Districts"
        verbose_name = "District"


class Sensortype(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sensortypes"
        verbose_name = "Sensortype"
