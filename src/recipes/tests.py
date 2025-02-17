from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Recipe
from .forms import RecipesSearchForm, AddRecipeForm

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name='Test Recipe',
            ingredients='Ingredient One, Ingredient Two, Ingredient Three, Ingredient Four',
            cooking_time=20,
        )

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'name')

    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length

        self.assertEqual(max_length, 50)

    def test_difficulty_calculation(self):
        recipe = Recipe.objects.get(id=1)
        
        self.assertEqual(recipe.difficulty, "Hard")

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

class AddRecipeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="12345")

    def setUp(self):
        self.client = Client()
        self.client.login(username="testuser", password="12345")

    def test_add_recipe_view_get(self):
        response = self.client.get(reverse("recipes:add_recipe"))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "recipes/add_recipe.html")

        self.assertIsInstance(response.context["add_recipe_form"], AddRecipeForm)

    def test_add_recipe_view_post_valid_data(self):
        data = {
            "name": "Test Recipe",
            "ingredients": "Test Ingredients",
            "cooking_time": 20,
            "pic": ""
        }

        response = self.client.post(reverse("recipes:add_recipe"), data)

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse("recipes:list"))

        self.assertEqual(Recipe.objects.count(), 1)

        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(len(messages), 1)

        self.assertEqual(str(messages[0]), "Recipe added successfully.")

    def test_add_recipe_view_post_invalid_data(self):
        data = {}

        response = self.client.post(reverse("recipes:add_recipe"), data)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "recipes/add_recipe.html")

        self.assertFalse(response.context["add_recipe_form"].is_valid())
