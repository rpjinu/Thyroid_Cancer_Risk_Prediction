from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("models/thyroid_cancer_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return "Thyroid Cancer Risk Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array([
            data['age'],
            1 if data['gender'].lower() == 'male' else 0,
            data['tsh_level'],
            data['t3_level'],
            data['t4_level'],
            data['nodules'],
            data['family_history']
        ]).reshape(1, -1)
        
        prediction = model.predict(features)[0]
        confidence = max(model.predict_proba(features)[0])
        
        result = "High Risk" if prediction == 1 else "Low Risk"
        
        return jsonify({"prediction": result, "confidence": round(confidence, 2)})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
