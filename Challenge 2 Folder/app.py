from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for API

# MySQL Configuration
app.config['MYSQL_HOST'] = 'sql100.infinityfree.com'
app.config['MYSQL_USER'] = 'if0_37961556'
app.config['MYSQL_PASSWORD'] = 'q9OwPfjJ8QXKy'
app.config['MYSQL_DB'] = 'if0_37961556_kitchen'

mysql = MySQL(app)

# API Route to Get Ingredients
@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ingredients")  # Replace 'ingredients' with your table name
    rows = cur.fetchall()
    ingredients = [{'id': row[0], 'name': row[1], 'quantity': row[2]} for row in rows]
    return jsonify(ingredients)

# API Route to Add Ingredient
@app.route('/ingredients', methods=['POST'])
def add_ingredient():
    data = request.get_json()
    name = data.get('name')
    quantity = data.get('quantity')
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO ingredients (name, quantity) VALUES (%s, %s)", (name, quantity))
    mysql.connection.commit()
    
    return jsonify({'message': 'Ingredient added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)

from apis.recipe_api import recipe_api
app.register_blueprint(recipe_api)

import openai

openai.api_key = 'your_openai_api_key'

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.get_json().get('message')
    response = openai.Completion.create(
        engine="gpt-4",  # Use the engine of your choice
        prompt=user_message,
        max_tokens=150
    )
    return jsonify({'response': response.choices[0].text.strip()})


