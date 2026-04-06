




from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
 
    image = models.ImageField(upload_to='category/', default='category/default.png')

    def __str__(self):
        return self.name



# Category is the name of your Python class, which will represent a database table and it inherits everything from Django model base class.
# models is a toolbox with all Django model tools
# Model is a base class for creating your own database tables and it provides all the built-in database features, like saving, querying, auto id fields, etc.
# __str__ is also special method in python that tells python how to represent object as a string .
# without special method , python shows the random memory address,
# With special method, python shows the human friendly memory address.
# __init__ is used for creating objects
