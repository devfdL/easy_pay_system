from django.db import models


# Create your models here.

class payment(models.Model):
    sender      = models.CharField(max_length = 100)
    place       = models.CharField(max_length = 100)
    nominal     = models.CharField(max_length = 50)
    date        = models.CharField(max_length = 50)

    published   = models.DateTimeField(auto_now_add = True)
    updated     = models.DateTimeField(auto_now = True)

    
    def __str__(self):
        return '{}, {}'.format(self.id,self.place)
