from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipe(models.Model):
    name= models.CharField(max_length=50)
    ingredients= models.CharField(
        max_length=225,
        help_text="Enter the ingredients , separated by a comma."
    )
    cooking_time= models.IntegerField()
    difficulty= None
    pic= models.ImageField(upload_to='recipes', default='no_picture.jpg')

    @property
    def difficulty(self):
        ingredients = self.ingredients.split(", ")

        if self.cooking_time < 10 and len(ingredients) < 4:
            return "Easy"
        elif self.cooking_time < 10 and len(ingredients) >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and len(ingredients) < 4:
            return "Intermediate"
        elif self.cooking_time >= 10 and len(ingredients) >= 4:
            return "Hard"
        return "Unknown"
    
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})