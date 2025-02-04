from django.db import models

# Create your models here.
class User(models.Model):
    username= models.CharField(max_length=50)
    password= models.TextField()
    email= models.TextField()
    pic= models.ImageField(upload_to='users', default='no_picture.jpg')

    def __str__(self):
        return str(self.username)