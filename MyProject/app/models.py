from django.db import models


class SulpakSmartphones(models.Model):
    name = models.CharField(max_length=500, blank=False, default='')
    current_price = models.CharField(max_length=200, blank=False, default='')


class SulpakSmartphonesHistory(models.Model):
    phone_id = models.ForeignKey(SulpakSmartphones, on_delete=models.CASCADE)
    price = models.CharField(max_length=200, blank=False, default='')
    time = models.TimeField(auto_now_add=True, blank=True)

