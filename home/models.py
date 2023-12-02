from django.db import models

# Create your models here.




from django.contrib.auth.models import User 

# Create your models here.

class Cars(models.Model):
    user = models.ForeignKey(User , on_delete = models.SET_NULL , null=True , blank=True)
    car_name = models.CharField(max_length=100)
    car_number = models.CharField(max_length=20)
    car_money = models.IntegerField()