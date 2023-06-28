
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home_food'),
    path('home/restaurant',views.home_restaurant,name='home_restaurant')
]