from django.db import models

# Create your models here.
class info(models.Model):
    name= models.CharField(max_length=100)
    depart_from= models.CharField(max_length=80)
    destination= models.CharField(max_length=80)
    depart_timing= models.TimeField()
    reach_timing= models.TimeField()
    seats= models.IntegerField()
    price = models.IntegerField()
    img= models.ImageField()
    date = models.DateField()

    def __str__(self): #to return name instead of info objects (1) in admin in account booked_flights
        return self.name