from django.db import models
from flights.models import info
from django.contrib.auth.models import auth,User

# Create your models here.
class booked_flights(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    flight_id = models.ForeignKey(info,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username +' booked '+ self.flight_id.name