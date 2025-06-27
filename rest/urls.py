from django.urls import path
from . import views

urlpatterns = [
path('food/',views.food,name='food'),
path('chef/',views.chef,name='chef'),
path('about/',views.about,name='about'),
path('',views.home,name='home'),
path('log/',views.log,name='log'),
path('rate/',views.rate,name='rate'),
path('allrating/',views.allrating,name='allrating'),
path('reservation/', views.reservation, name='reservation'),
path('stripe/', views.stripe, name='stripe'),






]