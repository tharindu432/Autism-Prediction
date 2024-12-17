import pandas as pd
import numpy as np
import pickle


class DataPreprocessor:
    def __init__(self, encoders_path):
        """
        Initialize the preprocessor with saved label encoders

        :param encoders_path: Path to saved encoders pickle file
        """
        with open(encoders_path, 'rb') as f:
            self.encoders = pickle.load(f)

    def preprocess_input(self, input_data):
        """
        Preprocess the input data for prediction

        :param input_data: Dictionary of input features
        :return: Processed numpy array ready for prediction
        """
        # Convert input to DataFrame
        df = pd.DataFrame([input_data])

        # Encode categorical columns
        categorical_columns = [
            'A1_Score', 'A2_Score', 'A3_Score', 'A4_Score', 'A5_Score',
            'A6_Score', 'A7_Score', 'A8_Score', 'A9_Score', 'A10_Score',
            'gender', 'ethnicity', 'jaundice', 'austim', 'contry_of_res',
            'used_app_before', 'relation'
        ]

        # Apply label encoding
        for col in categorical_columns:
            if col in self.encoders:
                df[col] = self.encoders[col].transform(df[col])

        # Remove any columns not in the original training data
        columns_to_drop = ['ID', 'age_desc', 'Class/ASD']
        df = df.drop(columns=columns_to_drop, errors='ignore')

        return df.values