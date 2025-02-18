from django import forms
from .models import Recipe

CHART__CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

class RecipesSearchForm(forms.Form):
    recipe_ingredients = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "name",
            "ingredients",
            "cooking_time",
            "pic"
        ]