from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, search, add_recipe

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('search/', search, name='search'),
    path('add_recipe/', add_recipe, name='add_recipe')
]