from django.db import models

# Create your models here.
class Dish(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        NOT_AVAILABLE = 'notavailable', 'Not Available'

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to="restaurant front")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.AVAILABLE)

    def __str__(self):
        return self.title

class Rating(models.Model):
    class Stars(models.TextChoices):
        star= '*','*'
        tstar= '**','**'
        thstar= '***','***'
        fostar= '****','****'
        fistar= '*****','*****'
        
    name=models.CharField(max_length=50)
    stars=models.CharField(choices=Stars.choices)
    img=models.ImageField(upload_to='restaurant front',null=True,blank=True)
    comment=models.TextField(max_length=1000)