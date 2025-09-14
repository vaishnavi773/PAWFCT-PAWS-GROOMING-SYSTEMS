from django.db import models

# Create your models here.
class serviceDB(models.Model):
    servicename=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=100, null=True, blank=True)
    image=models.ImageField(upload_to="image", null=True, blank=True)
