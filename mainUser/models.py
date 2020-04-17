from django.db import models
from django.contrib.auth.models import User
from django.core.validators import int_list_validator
# Create your models here.


ROLE_ADMIN = 0
ROLE_SHIPPER = 1
ROLE_CUSTOMER = 2




class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image =  models.ImageField(upload_to='imgs/profile/')
    roles = models.CharField(validators=[int_list_validator], max_length=100)
    def __str__(self):
        return self.user.username


class cars(models.Model):
    car_year = models.CharField(max_length=50)
    car_vin = models.CharField(max_length=50)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_state =  models.IntegerField(default=0)
    car_is_ok =  models.BooleanField(default=True)
    img =  models.ImageField(upload_to='imgs/cars/',default='404.jpg')

    def __str__(self):
        return self.car_vin