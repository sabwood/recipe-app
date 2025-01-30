from django.db import models

# Create your models here.
class User(models.Model):
    username= models.CharField(max_length=50)
    password= models.TextField()
    email= models.TextField()

    def __str__(self):
        return str(self.name)