from flask import Blueprint, request, jsonify
import pickle
import numpy as np

from app.utils.preprocessing import DataPreprocessor
import config

prediction_bp = Blueprint('prediction', __name__)

# Load model and preprocessor
with open(config.Config.MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

preprocessor = DataPreprocessor(config.Config.ENCODERS_PATH)


@prediction_bp.route('/predict', methods=['POST'])
def predict_autism():
    """
    Endpoint to predict autism based on input features

    Expected input JSON format:
    {
        "A1_Score": value,
        "A2_Score": value,
        ...
        "age": value,
        "result": value
    }
    """
    try:
        # Get input data
        input_data = request.get_json()

        # Preprocess input
        processed_input = preprocessor.preprocess_input(input_data)

        # Make prediction
        prediction = model.predict(processed_input)
        probability = model.predict_proba(processed_input)

        # Prepare response
        return jsonify({
            'prediction': int(prediction[0]),
            'probability': float(np.max(probability[0])),
            'class_labels': {
                0: 'No Autism',
                1: 'Autism Detected'
            }
        }), 200

    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Error in making prediction'
        }), 400


@prediction_bp.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Autism Detection API is running'
    }), 200