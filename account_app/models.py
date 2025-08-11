from django.db import models
from django.contrib.auth.models import User
from car_app.models import CarModel

# Create your models here.
class CommentModel(models.Model):
       name = models.CharField(max_length=30)
       text = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
              return f"{self.name}"
       

class UserProfileModel(models.Model):
       user = models.OneToOneField(User,on_delete=models.CASCADE)
       # purchased_cars = models.ManyToManyField(CarModel,blank=True)

       def __str__(self):
        return f'{self.user.username} Profile'
       

class PurchaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} bought {self.car.car_title}"