from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import Group

# User Models
class User(AbstractUser):
    username = models.CharField(max_length=50, blank= True)
    email = models.EmailField(unique = True)
    is_farmer = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


# Farm Models
class Town(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # def farm_count(self):
    #     return Farm.count(town = self)


class Farm(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    produce = models.CharField(max_length = 500)
    address = models.CharField(max_length = 500)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    