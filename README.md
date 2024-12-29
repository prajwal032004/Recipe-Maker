# Recipe Finder App 🥞🍩

This is a Flask-based web application that allows users to search for recipes using the Spoonacular API. Users can search for recipes by keywords, view detailed recipe information, and get cooking instructions.

## Features

- Search for recipes using keywords.
- View a list of matching recipes with brief details.
- Click on a recipe to view detailed information, including ingredients and instructions.

## Prerequisites

1. **Python**: Ensure you have Python 3.7+ installed.
2. **Spoonacular API Key**: Sign up at [Spoonacular](https://spoonacular.com/food-api) to get your own API key.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/prajwal032004/recipe-finder-app.git
   cd recipe-finder-app
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Replace the `API_KEY` in `app.py` with your Spoonacular API key:
   ```python
   API_KEY = 'your_spoonacular_api_key'
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

3. Use the search bar to find recipes or click on a recipe to view more details.

## Routes

### Home Page
**Path:** `/home`  
**Method:** `GET`  
Renders the homepage with an empty search query and no recipes displayed initially.

### Main Page
**Path:** `/`  
**Method:** `GET`, `POST`  
- **POST**: Handles recipe search queries submitted via the search form and fetches matching recipes.
- **GET**: Displays recipes based on the `search_query` parameter or an empty search if none is provided.

### View Recipe
**Path:** `/recipe/<int:recipe_id>`  
**Method:** `GET`  
Fetches detailed information about a specific recipe using its `recipe_id` and displays the details along with cooking instructions.

## File Structure

- **app.py**: The main application file containing routes and logic.
- **templates/**: Contains HTML templates for rendering pages.
  - `index.html`: The homepage template for search and results.
  - `view_recipe.html`: Template for detailed recipe information.
- **static/**: (Optional) Add static files like CSS or JavaScript here.

## Dependencies

The dependencies are listed in `requirements.txt`. Install them using `pip install -r requirements.txt`.

## Screenshots

Include screenshots of the app (search page and recipe details page) for better understanding.

## License

This project is licensed under the Self License. See the LICENSE file for details.

---

### Note:
Make sure to get your own API key from [Spoonacular](https://spoonacular.com/food-api) and replace the placeholder in `app.py`.

Happy Coding!
