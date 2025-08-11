from django.db import models
from brand_app.models import BrandModel

# Create your models here.
class CarModel(models.Model):
    car_title = models.CharField(max_length=50)
    car_description = models.TextField(max_length=350)
    car_img = models.ImageField(upload_to='media_files/' , blank=True, null=True)
    car_price = models.CharField()
    car_quantity = models.IntegerField()

    brand = models.ForeignKey(BrandModel,on_delete=models.CASCADE , null=True, blank=True)

    def __str__(self):
        return f"{self.car_title}"
