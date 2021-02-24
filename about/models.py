from django.db import models

# Create your models here.
class Members(models.Model):
    name= models.CharField(max_length=50)
    age = models.IntegerField()
    div= models.CharField(max_length=1)
    srno= models.IntegerField()
    email= models.EmailField(max_length = 254) 
    role= models.TextField()

    def __str__(self):
        return self.name

class testMember :
    id : int
    name: str
    age : int
    div: str
    srno : int
    role : str