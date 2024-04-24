from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
from datetime import date

class Car(models.Model):

    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100, blank=True)
    rok = models.DateField(default=date.today)
    automat = models.BooleanField(default=None)
    cena = models.IntegerField(default=1000)
    dostępność = models.BooleanField(default=True)

    def __str__(self):
        return self.marka

    def is_old_car(self):
        """Czy auto jest starsze niż 10 lat."""
        return (datetime.now().date() - self.rok) <= timedelta(days=3650)
    
    def car_representation(self):
        """Zwraca markę, model, rok i cenę auta"""
        return f"{self.marka} by {self.model} by {self.rok} by {self.cena}"

    def get_absolute_url(self):
        """Generuje URL do szczegółów auta."""
        return reverse('car-detail', kwargs={'pk': self.pk})

    def reserve(self):
        """Rezerwuje samochód (zmienia dostępność na False)."""
        self.dostępność = False
        self.save()

        