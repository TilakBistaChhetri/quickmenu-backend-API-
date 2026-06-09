




# from django.db import models

# class Restaurant(models.Model):
#     name = models.CharField(max_length= 20)

#     def __str__(self):
#         return self.name


from django.contrib.auth.models import User
from django.db import models

class Restaurant(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    



    

# OneToOneField is also field in Django model, But it is a special type of field , it is not simple field but it is a relationship field
#OneToOneField is used to connect two table.

      