# KUET-BitFest-Hackathon-Preli-Solutions

# Challenge 1: Banglish-to-Bengali Transliteration
Iqbal’s laptop has been compromised by an evil hacker who uninstalled the Avro keyboard, rendering him unable to type in Bengali. Unfortunately, reinstalling the keyboard isn’t an option. In order to help him win a heated Facebook comment debate, Iqbal decides to train a model that can convert Banglish text (Bengali written in English letters) into the correct Bengali script.

## Dataset
We used the SKNahin/bengali-transliteration-data dataset available on Hugging Face, which contains pairs of Banglish and Bengali text. This dataset is ideal for training a model to perform transliteration from Banglish to proper Bengali script.

## Tasks
#### 1. Loading the Dataset
The dataset is loaded from the Hugging Face library using the load_dataset function. The data is then split into training and validation sets, with a typical split ratio of 90/10 for training and validation datasets respectively.

#### 2. Data Preprocessing
To prepare the dataset for training, we needed to tokenize both the Banglish and Bengali text. We used the T5 tokenizer, which is suitable for sequence-to-sequence tasks. The tokenizer pads and truncates the sentences to a fixed length of 128 tokens, ensuring uniformity. We mapped the processed data to both the training and validation datasets.

#### 3. Selecting a Model
We used the T5ForConditionalGeneration model, a pre-trained sequence-to-sequence model, available from Hugging Face. T5 is a versatile model capable of performing a variety of tasks, including translation and transliteration. The choice of T5 is based on its efficiency and effectiveness for low-resource language tasks such as Banglish-to-Bengali transliteration.

#### 4. Training the Model
We fine-tuned the pre-trained T5 model on the Banglish-to-Bengali dataset. We set up the training pipeline using the Hugging Face Trainer class. The hyperparameters, including learning rate, batch size, and number of epochs, are chosen to balance model performance and training time.

### Model Link : <i> https://huggingface.co/Khalid751/Banglish-to-Bengali-Transliteration </i>

## Key Considerations:
Dataset Preprocessing: We ensured that the Banglish and Bengali text are tokenized correctly, maintaining a consistent sequence length across all input and output samples. <br>
Model Choice: T5 is selected due to its strong performance on sequence-to-sequence tasks, especially in multilingual settings, which suits the task of transliterating from Banglish to Bengali. <br>
Training Pipeline: The pipeline uses standard deep learning techniques, including weight decay and saving checkpoints, ensuring efficient training and model evaluation. <br>
By following this pipeline, the model is trained to perform accurate Banglish-to-Bengali transliteration, which can be useful for users like Iqbal who need to write in Bengali without having the proper keyboard installed.


# Challenge 2: Mofa's Kitchen Buddy

Mofa's Kitchen Buddy is a backend system that helps Mofa manage his ingredients and suggests recipes based on what he has at home. The system includes APIs for ingredient management, recipe retrieval, and a chatbot powered by a large language model (LLM) to suggest recipes based on available ingredients and personal preferences.

## Project Structure

```
Mofa_Kitchen_Buddy/
├── app.py                  # Main Flask application
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── apis/
    └── recipe_api.py       # API routes for recipe management
└── database/
    └── models.py           # Database models for ingredients and recipes
└── tests/
    └── test_app.py         # Unit tests for API routes
```

## Features
1. Ingredient Management API:
   - Add and manage available ingredients in the database.
   - Update inventory after shopping or cooking.
2. Recipe Retrieval System:
   - Store and retrieve recipes saved in a combined text file (`my_fav_recipes.txt`).
   - Allow users to input new favorite recipes (either as text or images).
3. Chatbot Integration:
   - A chatbot integrated with an LLM (e.g., GPT-3/4) to suggest recipes based on ingredients available at home.
   - Chatbot understands preferences such as "I want something sweet" or "I want to cook a dinner".

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Mofa_Kitchen_Buddy.git
   cd Mofa_Kitchen_Buddy
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
In `app.py`, the MySQL database connection is configured using the following credentials:
```python
app.config['MYSQL_HOST'] = 'sql100.infinityfree.com'
app.config['MYSQL_USER'] = 'if0_37961556'
app.config['MYSQL_PASSWORD'] = 'eDYGY9TX*7f/g(-'
app.config['MYSQL_DB'] = 'if0_37961556_kitchen'
```

Ensure the database is correctly set up on your server using `phpMyAdmin` or any MySQL interface.

## API Documentation
### Ingredient Management API
#### Route: `/ingredients`
**Method**: `GET`
This endpoint retrieves all available ingredients from the database.

**Sample Response**:
```json
[
    {
        "id": 1,
        "name": "Tomato",
        "quantity": 10
    },
    {
        "id": 2,
        "name": "Potato",
        "quantity": 5
    }
]
```
#### Route: `/ingredients`
**Method**: `POST`
This endpoint allows you to add a new ingredient to the database.

**Sample Payload**:
```json
{
    "name": "Carrot",
    "quantity": 8
}
```
**Sample Response**:
```json
{
    "message": "Ingredient added successfully"
}
```

### Recipe Management API
#### Route: `/recipes`
**Method**: `GET`
This endpoint retrieves all stored recipes. Recipes are fetched from a combined `my_fav_recipes.txt` file.
**Sample Response**:
```json
[
    {
        "recipe_id": 1,
        "name": "Tomato Soup",
        "cuisine": "Italian",
        "taste": "Savory",
        "reviews": 5,
        "prep_time": "30 minutes"
    },
    {
        "recipe_id": 2,
        "name": "Vegetable Salad",
        "cuisine": "American",
        "taste": "Fresh",
        "reviews": 4,
        "prep_time": "15 minutes"
    }
]
```

#### Route: `/recipes`
**Method**: `POST`
This endpoint allows users to input a new recipe (either text or image) to be saved in the system.

**Sample Payload**:
```json
{
    "name": "Pasta Alfredo",
    "cuisine": "Italian",
    "taste": "Creamy",
    "reviews": 4,
    "prep_time": "20 minutes"
}
```

**Sample Response**:
```json
{
    "message": "Recipe added successfully"
}
```

### Chatbot API

#### Route: `/chatbot`
**Method**: `POST`

This endpoint interacts with the user to suggest recipes based on their preferences and the available ingredients in the kitchen.

**Sample Payload**:
```json
{
    "message": "I want something sweet today"
}
```

**Sample Response**:
```json
{
    "response": "You can try making a Chocolate Cake or Fruit Salad. Both are sweet and easy to prepare!"
}
```

## Database Schema

The database schema is designed to manage the ingredients and recipes.

### Ingredients Table
```sql
CREATE TABLE ingredients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL
);
```

### Recipes Table
```sql
CREATE TABLE recipes (
    recipe_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cuisine VARCHAR(100),
    taste VARCHAR(100),
    reviews INT,
    prep_time VARCHAR(100)
);
```

## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. The server will run locally at `http://127.0.0.1:5000`. You can now test the APIs using Postman or any other tool.

## Notes

- **Database**: Make sure you have configured your database credentials correctly. You may need to create the tables before running the app.
- **Recipe File**: The combined `my_fav_recipes.txt` file contains all your favorite recipes. You can manually add recipes in the text file or input them through the API.
- **Chatbot**: The chatbot interacts with the user to provide personalized recipe suggestions based on the ingredients available and user preferences.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
