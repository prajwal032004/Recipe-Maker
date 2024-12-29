from flask import Flask, render_template, request
import requests
from urllib.parse import unquote

# Create the Flask app
app = Flask(__name__)

# Replace with your Spoonacular API key
API_KEY = 'your_spoonacular_api_key'

# Define the route for the home page
@app.route('/home', methods=['GET'])
def home():
    # Render the main page with empty recipe list and search query
    return render_template('index.html', recipes=[], search_query='')

# Define the main route for the app
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the search query from the form
        query = request.form.get('search_query', '').strip()
        # Fetch recipes based on the query
        recipes = search_recipes(query)
        # Render the main page with search results
        return render_template('index.html', recipes=recipes, search_query=query)

    # Handle GET requests or empty form submissions
    search_query = request.args.get('search_query', '').strip()
    decoded_query = unquote(search_query)
    recipes = search_recipes(decoded_query)
    return render_template('index.html', recipes=recipes, search_query=decoded_query)

# Function to search for recipes based on the provided query
def search_recipes(query):
    if not query:
        # Return an empty list if the query is empty
        return []
    
    # Define the API endpoint and parameters
    url = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': 10,
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }

    try:
        # Send a GET request to the Spoonacular API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data.get('results', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recipes: {e}")
        return []

# Route to view a specific recipe by its ID
@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    # Get the search query from the URL
    search_query = request.args.get('search_query', '')
    # Define the API endpoint for fetching recipe information
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {'apiKey': API_KEY}

    try:
        # Send a GET request to the Spoonacular API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        recipe = response.json()
        return render_template('view_recipe.html', recipe=recipe, search_query=search_query)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recipe details: {e}")
        return "Recipe not found", 404

# Run the app in debug mode if executed directly
if __name__ == '__main__':
    app.run(debug=True,port=8000)
