from django.db import models

# Create your models here.
class Dish(models.Model):
    class B(models.TextChoices):
        Best='best','best'
        Nonbest='Nonbest','Nonbest'


    class Status(models.TextChoices):
        exist = 'exist', 'exist'
        none = 'none', 'none'
    class C(models.TextChoices):
        Dessert = 'dessert', 'dessert'
        Seefood = 'Seefood', 'Seefood'
        Spicyfood= 'spicy','spicy'
        healthyfood='healthyfood','healthyfood'
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to="brest")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.exist)
    category=models.CharField(choices=C.choices ,null=True,blank=True)
    best=models.CharField(choices=B.choices,null=True,blank=True)

    def __str__(self):
        return self.title

class Rating(models.Model):
    class Stars(models.TextChoices):
        star= '*','*'
        tstar= '**','**'
        thstar= '***','***'
        fostar= '****','****'
        fistar= '*****','*****'
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE, related_name='ratings' ,null=True,blank=True)
    name=models.CharField(max_length=50 ,null=True,blank=True)
    stars=models.CharField(choices=Stars.choices ,null=True,blank=True)
    img=models.ImageField(upload_to='restaurant front',null=True,blank=True )
    comment=models.TextField(max_length=1000 ,null=True,blank=True)







class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    guests = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)