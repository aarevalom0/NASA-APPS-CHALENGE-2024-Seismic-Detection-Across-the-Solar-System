from flask import Flask, render_template, request, jsonify, redirect
import pandas as pd
import joblib  # Assuming you're using a pre-trained model
import os

app = Flask(__name__)

# Load your pre-trained model
model = joblib.load('modelo_seleccionado.pkl')  # Ensure this points to your trained model file

# Route for the homepage (with the form)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the CSV upload and prediction
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400  # No file uploaded
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400  # No file selected
        
        if file and file.filename.endswith('.csv'):  # Check if it's a CSV
            try:
                # Load the CSV into a DataFrame
                data = pd.read_csv(file)

                # Use your model to make predictions
                predictions = model.predict(data)

                # Return predictions as JSON (or render a results page)
                return jsonify({'predictions': predictions.tolist()})

            except Exception as e:
                return jsonify({'error': f"Error processing file: {str(e)}"}), 500

        return jsonify({'error': 'Invalid file type. Only CSVs are allowed.'}), 400

if __name__ == "__main__":
    app.run(debug=True)