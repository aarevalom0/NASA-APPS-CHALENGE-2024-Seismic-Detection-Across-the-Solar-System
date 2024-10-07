from flask import Flask, render_template, request, redirect, jsonify
import pandas as pd
import joblib  # Assuming you're using a pre-trained model
import os

app = Flask(__name__)

# Load your pre-trained model
model = joblib.load('modelo_seleccionado.pkl')  # Use your trained model file

# Home route to display the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the CSV upload and prediction
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect('/')
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect('/')
    
    if file:
        # Assuming the file is a CSV, load it into a DataFrame
        data = pd.read_csv(file)
        
        # Make predictions using your model
        predictions = model.predict(data)
        
        # Convert predictions to a format you can return (e.g., a list or JSON)
        results = {'predictions': predictions.tolist()}
        
        # Return the predictions as a JSON response
        return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)