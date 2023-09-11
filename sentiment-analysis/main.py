"""
Problem Statement:
Develop a sentiment analysis tool that can classify tweets or reviews into positive, negative, or neutral categories. 
The solution should be based on a machine learning model trained on a labeled dataset of tweets/reviews.

Note: For a real-world application, one would use a large labeled dataset to train the model. 
For simplicity, we are using a small sample dataset in this example.
"""

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Sample dataset: (tweet/review, sentiment)
# sentiment: 0 - negative, 1 - neutral, 2 - positive
data = [
    ("This product is amazing!", 2),
    ("I hate this show.", 0),
    ("It's okay, not the best.", 1),
    ("Loved the experience!", 2),
    ("Never buying this again!", 0),
    ("It's average, nothing special.", 1),
]

# Convert data to DataFrame
df = pd.DataFrame(data, columns=['text', 'sentiment'])

# Split data into training and testing set
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['sentiment'], test_size=0.2, random_state=42)

# Convert text data into feature vectors
vectorizer = CountVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_vec, y_train)

# Predict on the test set
y_pred = clf.predict(X_test_vec)

# Print classification report
print(classification_report(y_test, y_pred, target_names=['negative', 'neutral', 'positive']))

def predict_sentiment(text):
    """
    Predicts the sentiment of a given text.
    """
    vec_text = vectorizer.transform([text])
    sentiment = clf.predict(vec_text)[0]
    sentiment_mapping = {0: 'negative', 1: 'neutral', 2: 'positive'}
    return sentiment_mapping[sentiment]

# Test the prediction function
sample_text = "I really enjoyed this!"
print(f"The sentiment of the text '{sample_text}' is: {predict_sentiment(sample_text)}")
