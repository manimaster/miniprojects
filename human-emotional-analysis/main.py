# Train or obtain a pre-trained emotion detection model. You can use datasets like CK+, FER2013, or AffectNet to train your own model or find pre-trained models online.
# Save the pre-trained model as 'emotion_model.h5' in the same directory as your Python script.

import cv2
import numpy as np
from keras.models import load_model

# Load a pre-trained emotion detection model
model = load_model('emotion_model.h5')

# Define the emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Load and preprocess the input image
def preprocess_image(image_path):
    img = cv2.imread(image_path, 0)  # Load image in grayscale
    img = cv2.resize(img, (48, 48))  # Resize image to model input size (48x48 pixels)
    img = img / 255.0  # Normalize pixel values to range [0, 1]
    img = np.reshape(img, (1, 48, 48, 1))  # Reshape for model input
    return img

# Perform emotion analysis on the input image
def analyze_emotion(image_path):
    img = preprocess_image(image_path)
    emotion_probs = model.predict(img)
    emotion_id = np.argmax(emotion_probs)
    emotion = emotion_labels[emotion_id]
    return emotion

# Path to the input image
input_image_path = 'sample_face.jpg'  # Replace with the path to your image

# Analyze the emotion in the input image
result = analyze_emotion(input_image_path)
print(f"Emotion in the image: {result}")
