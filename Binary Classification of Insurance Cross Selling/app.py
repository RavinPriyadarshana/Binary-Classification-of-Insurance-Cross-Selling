from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model
with open('static\model\insurence_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize the Flask application
app = Flask(_name_)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')  # You need to create an index.html file for the user interface

# Define the predict route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the form
    customer_data = [float(x) for x in request.form.values()]

    # Convert the data into a NumPy array
    data_array = np.array([customer_data])

    # Make a prediction using the loaded model
    prediction = model.predict(data_array)[0]

    # Render the result on the page
    return render_template('index.html', prediction_text=f'Customer Response: {"Yes" if prediction == 1 else "No"}')

# Run the application
if _name_ == '_main_':
    app.run(debug=True)