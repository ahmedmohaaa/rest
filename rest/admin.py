from django.contrib import admin
from .models import Dish,Rating,Reservation
# Register your models here.
admin.site.register(Dish)
admin.site.register(Rating)
admin.site.register(Reservation)

