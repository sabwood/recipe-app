# Django Recipe App:

## Project Overview:
This project is a web application with multiple users and an admin panel, using Python-based Django framework. This recipe app aims to allow users to create and modify recipes containing ingredients, cooking time, and a difficulty parameter automatically calculated by the application. The users should also be able to search for recipes by ingredient.

## Key Features:
 - User Authentication: Login and logout functions
 - Search By Ingredient Function
 - Add Recipe Function
 - Difficulty Calculation: When users add recipes, the application calculates the difficulty of recipes based on cooking time and number of ingredients.
 - Django Admin Dashboard
 - Chart Statistics and Visualizations: Based on user-inputted search criteria

## Technical Requirements:
 - Python 3.6+
 - Django (version 3)
 - PostgreSQL

## Set Up and Installation:
1. Clone the repository
   ```bash
   git clone <https://github.com/sabwood/recipe-app>
   ```
2. Create and activate virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   py manage.py migrate
   ```
5. Run development server:
   ```bash
   py manage.py runserver
   ```
