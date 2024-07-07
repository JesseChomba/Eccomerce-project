from django.db import models

# Create your models here.
class Products(models.model):
    name = models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='products/')
    Availability = models.BooleanField(default=True)

    def _str_(self):
        return self.name