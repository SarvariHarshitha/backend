from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image
import os

file_path = "model.h5"

print("Current Working Directory:", os.getcwd())
print("File Exists:", os.path.exists(file_path))


app = Flask(__name__)
CORS(app)


model = load_model("model.h5") 

@app.route('/health', methods = ['GET'])
def health():
    text = 'koushik'
    return jsonify({'prediction': text })

def preprocess_image(image, target_size):
    image = Image.open(image)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image = image.resize(target_size)
    image = img_to_array(image)  
    image = image / 255.0      
    image = np.expand_dims(image, axis=0) 
    return image

@app.route('/predict', methods=['POST'])
def predict():
    image = request.files['file']
    name = request.form.get('name')
    email = request.form.get('email')
    processed_image = preprocess_image(image, target_size=(224, 224))
    prediction = model.predict(processed_image)
    label = np.argmax(prediction, axis=1)[0]
    index = ['Mild Demented', 'Moderate Demented', 'Non Demented', 'Very Mild Demented']
    
    return jsonify({'prediction': index[label]})

if __name__ == '__main__':
    app.run(debug=True)
