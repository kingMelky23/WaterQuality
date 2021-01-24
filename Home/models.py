from django.db import models


# Create your models here.

class Zipcode(models.Model):
    areaCode = models.TextField('zipcode')
    entered = models.DateTimeField('date published')
