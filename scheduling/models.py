from django.db import models

# Create your models here.

from django.db import models

class BarberShop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    client_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    barber_shop = models.ForeignKey(BarberShop, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.client_name} - {self.date} {self.time}'
