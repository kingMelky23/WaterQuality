from django.db import models


# Create your models here.

class Zipcode(models.Model):

    areaCode = models.TextField('zipcode', max_length=5)
    entered = models.DateTimeField('date published')

    def __str__(self):
        return self.areaCode
