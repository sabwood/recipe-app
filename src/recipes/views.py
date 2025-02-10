from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipesSearchForm
from .models import Recipe
from .utils import get_chart
import pandas as pd

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipe-list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe-detail.html'

@login_required
def search(request):
    form = RecipesSearchForm(request.POST or None)
    recipes_df = None
    chart = None

    if request.method == 'POST':
        recipe_difficulty = request.POST.get('recipe_difficulty')
        chart_type = request.POST.get('chart_type')

        qs = Recipe.objects.filter(difficulty=recipe_difficulty)

        if qs:
            recipes_df = pd.DataFrame(qs.values())

            chart = get_chart(chart_type, recipes_df, labels=recipes_df['ingredients'].values)

            recipes_df = recipes_df.to_html()

    context = {
        "form": form,
        "recipes_df": recipes_df,
        "chart": chart
    }

    return render(request, 'recipes/search.html', context)