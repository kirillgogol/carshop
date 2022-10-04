from dataclasses import field
from email.mime import image
from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User

class Car(models.Model):
    brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    year = models.IntegerField(default=2010, 
    validators=[ MaxValueValidator(timezone.now().year), MinValueValidator(2010)]
    )
    photo = models.ImageField(upload_to='photos/', default='photos/car.png')
    cost = models.IntegerField(default=10000, 
    validators=[ MaxValueValidator(2000000), MinValueValidator(10000)]
    )

    def __str__(self):
        return self.brand + " " + self.car_model


class TechSpec(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    weight = models.IntegerField(default=1250, 
        validators=[ MaxValueValidator(2500), MinValueValidator(1250)]
    )
    wheel_drive_type = models.CharField(max_length=10)
    hp = models.IntegerField(default=100, 
        validators=[ MaxValueValidator(800), MinValueValidator(100)]
    )
    engine_type = models.CharField(default="Petrol", max_length=10)



class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    # name = models.CharField(max_length=80)
    header = models.TextField(max_length=40, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) + ") " + "Header:" + str(self.header)
