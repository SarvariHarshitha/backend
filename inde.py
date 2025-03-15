from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image

# Path to the image
img = "moderate.jpg"

print("----------------------------------------------------")
print("----------------------------------------------------")
print("Started")

# Preprocessing function
def preprocess_image(image_path, target_size):
    image = Image.open(image_path)  # Open image from file path
    if image.mode != 'RGB':
        image = image.convert('RGB')  # Ensure it's in RGB mode
    image = image.resize(target_size)  # Resize image
    image = img_to_array(image)  # Convert to array
    image = image / 255.0  # Normalize to range [0, 1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Prediction function
def predict(image_path, model):
    processed_image = preprocess_image(image_path, target_size=(224, 224))  # Resize and preprocess
    prediction = model.predict(processed_image)  # Model prediction
    label = np.argmax(prediction, axis=1)[0]  # Get index of highest probability
    confidence = np.max(prediction)  # Get highest probability
    return label, confidence

# Load the model
model = load_model("model.h5")

# Class indices
index = ['Mild Demented', 'Moderate Demented', 'Non Demented', 'Very Mild Demented']

# Perform prediction
label, confidence = predict(img, model)

print("----------------------------------------------------")
print("----------------------------------------------------")
print()
print(f"Prediction: {index[label]} with confidence: {confidence:.2f}")

