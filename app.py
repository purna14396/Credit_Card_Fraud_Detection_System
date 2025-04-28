from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('credit_card_fraud_detection_model.pkl', 'rb'))

# Initialize the scaler for 'Amount' feature if required (dummy here)
scaler = StandardScaler()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        input_data = request.form['input_data']
        
        try:
            # Split the input and convert to float
            input_list = list(map(float, input_data.strip().split()))
            
            # Check if 30 values are provided
            if len(input_list) != 30:
                prediction = "Error: Please enter exactly 30 values (including Time)."
            else:
                # Remove the first value (Time)
                input_list = input_list[1:]
                
                # Reshape for prediction
                input_array = np.array(input_list).reshape(1, -1)
                
                # Predict
                pred = model.predict(input_array)
                prediction = "Fraudulent Transaction" if pred[0] == 1 else "Genuine Transaction"
        except Exception as e:
            prediction = f"Invalid input! Error: {e}"

    return render_template('predict.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
