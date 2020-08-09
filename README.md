# Chatbot
Retrieval Based Chatbot.
This chat bot used to read the input from the user and predict the output using Deep learning ML technique.

We have a Input intent file as a input, it has patterns and responses. The bot once receive the user input it will through the corresponding correct responses to the user questions.  


Below are the chatbot evaluation steps,
1. Data Exploration:   Know the data
	Intents.json (patterns and responses)
2. Data Pre-processing: Clean up the data and Normalization
	Using Tokenization and Stemming techniques to understand the meaning and the relationship between the words. (NLTK tokenization and LancasterStemmer)
3. Model : Deep Neural Network Model
	Neural networks understand numbers so we need to convert strings in intent file to numbers.
	Bags of words it represent any given pattern. Bags of words is one hard encoding meaning it has 0's and 1's
	Then the real machine learning part
	Having one input layer and two hidden layer(8) and an output layer.
	Then create a model with Deep Neural Network (DNN) and fit the model for training.
4. Training: Compile, fit, evaluate and predict
	Then using this model we can predict the output.

Using Flask to create a Front End UI.


Python Packages Versions:

Numpy        ==1.16.1
Tensorflow ==1.2.0
Tflearn        ==0.3.2
Nltk             ==3.5
