from django.db import models


# Create your models here.

class addCustomer(models.Model):
    u_name      = models.CharField(max_length = 100)
    f_name      = models.CharField(max_length = 100)
    l_name      = models.CharField(max_length = 100)
    birthday    = models.CharField(max_length = 50)

    published   = models.DateTimeField(auto_now_add = True)
    updated     = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return '{}, {}'.format(self.id,self.u_name,self.f_name)