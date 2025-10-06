from django.db import models

# Create your models here.
class serviceDB(models.Model):
    servicename = models.CharField(max_length=200)
    description = models.TextField(default="Not Provided")
    image = models.ImageField(upload_to='services/', default='default.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # <-- added

 
 