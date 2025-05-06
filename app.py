from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

# Flask application instance
app = Flask(__name__)  # This is the 'app' that Gunicorn is trying to find

model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    # For local testing purposes
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
