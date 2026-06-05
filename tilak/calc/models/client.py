
from django.db import models
from django.contrib.auth.models import User



class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    businessName = models.CharField(max_length=100),
     
    def __str__(self):
       return self.businessName
    
    


# OneToOneField is also field in Django model, But it is a special type of field , it is not simple field but it is a relationship field
#OneToOneField is used to connect two table.

      




