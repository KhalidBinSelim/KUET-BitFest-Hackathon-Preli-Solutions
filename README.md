# KUET-BitFest-Hackathon-Preli-Solutions

# Challenge 1: Banglish-to-Bengali Transliteration
Iqbal’s laptop has been compromised by an evil hacker who uninstalled the Avro keyboard, rendering him unable to type in Bengali. Unfortunately, reinstalling the keyboard isn’t an option. In order to help him win a heated Facebook comment debate, Iqbal decides to train a model that can convert Banglish text (Bengali written in English letters) into the correct Bengali script.

## Dataset
We used the SKNahin/bengali-transliteration-data dataset available on Hugging Face, which contains pairs of Banglish and Bengali text. This dataset is ideal for training a model to perform transliteration from Banglish to proper Bengali script.

## Tasks
#### 1. Load the Dataset
The dataset is loaded from the Hugging Face library using the load_dataset function. The data is then split into training and validation sets, with a typical split ratio of 90/10 for training and validation datasets respectively.

#### 2. Data Preprocessing
To prepare the dataset for training, we needed to tokenize both the Banglish and Bengali text. We used the T5 tokenizer, which is suitable for sequence-to-sequence tasks. The tokenizer pads and truncates the sentences to a fixed length of 128 tokens, ensuring uniformity. We mapped the processed data to both the training and validation datasets.

#### 3. Select a Model
We used the T5ForConditionalGeneration model, a pre-trained sequence-to-sequence model, available from Hugging Face. T5 is a versatile model capable of performing a variety of tasks, including translation and transliteration. The choice of T5 is based on its efficiency and effectiveness for low-resource language tasks such as Banglish-to-Bengali transliteration.

#### 4. Train the Model
We fine-tune the pre-trained T5 model on the Banglish-to-Bengali dataset. We set up the training pipeline using the Hugging Face Trainer class. The hyperparameters, including learning rate, batch size, and number of epochs, are chosen to balance model performance and training time.

### Model Link : <i> https://huggingface.co/Khalid751/Banglish-to-Bengali-Transliteration </i>

## Key Considerations:
Dataset Preprocessing: We ensured that the Banglish and Bengali text are tokenized correctly, maintaining a consistent sequence length across all input and output samples. <br>
Model Choice: T5 is selected due to its strong performance on sequence-to-sequence tasks, especially in multilingual settings, which suits the task of transliterating from Banglish to Bengali. <br>
Training Pipeline: The pipeline uses standard deep learning techniques, including weight decay and saving checkpoints, ensuring efficient training and model evaluation. <br>
By following this pipeline, the model is trained to perform accurate Banglish-to-Bengali transliteration, which can be useful for users like Iqbal who need to write in Bengali without having the proper keyboard installed.
