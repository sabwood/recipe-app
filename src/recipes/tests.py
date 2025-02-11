from django.test import TestCase
from .models import Recipe
from .forms import RecipesSearchForm

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name='Test Recipe',
            ingredients='Ingredient One, Ingredient Two, Ingredient Three, Ingredient Four',
            cooking_time=20,
            difficulty='Hard'
        )

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'name')

    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length

        self.assertEqual(max_length, 50)

    def test_difficulty_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('difficulty').max_length

        self.assertEqual(max_length, 20)

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

class RecipeFormTest(TestCase):
    def test_search_form_valid_data(self):
        form = RecipesSearchForm(
            data = {
                "recipe_ingredients": "Flour",
                "chart_type": "#1"
            }
        )

        self.assertTrue(form.is_valid())