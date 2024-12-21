from flask import Blueprint, jsonify, request

recipe_api = Blueprint('recipe_api', __name__)

@recipe_api.route('/recipes', methods=['GET'])
def get_recipe_suggestions():
    available_ingredients = request.args.get('ingredients').split(',')
    # Example mock response for recipe suggestions
    recipes = {
        "recipe_1": "Tomato Soup",
        "recipe_2": "Vegetable Salad"
    }
    return jsonify(recipes)


