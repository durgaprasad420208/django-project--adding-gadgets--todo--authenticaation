from django.db import models

# Create your models here.


class Computer(models.Model):
    brand = models.ForeignKey("computer.Brand", on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)
    rom = models.CharField(max_length=50)
    processor = models.CharField(default="i5", max_length=50)

    def __str__(self):
        return self.brand.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
