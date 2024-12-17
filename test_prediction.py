import requests
import json


def get_user_input():
    """
    Get input data from the user via terminal with correct label encoding
    """
    input_data = {
        "A1_Score": int(input("Enter A1_Score (0 or 1): ")),
        "A2_Score": int(input("Enter A2_Score (0 or 1): ")),
        "A3_Score": int(input("Enter A3_Score (0 or 1): ")),
        "A4_Score": int(input("Enter A4_Score (0 or 1): ")),
        "A5_Score": int(input("Enter A5_Score (0 or 1): ")),
        "A6_Score": int(input("Enter A6_Score (0 or 1): ")),
        "A7_Score": int(input("Enter A7_Score (0 or 1): ")),
        "A8_Score": int(input("Enter A8_Score (0 or 1): ")),
        "A9_Score": int(input("Enter A9_Score (0 or 1): ")),
        "A10_Score": int(input("Enter A10_Score (0 or 1): ")),
        "age": int(input("Enter age: ")),
        "result": int(input("Enter result: ")),

        # Gender options
        "gender": input("Enter gender (f/m): ").lower(),

        # Ethnicity options
        "ethnicity": input(
            "Enter ethnicity (Asian/Black/Hispanic/Latino/Middle Eastern/Others/Pasifika/South Asian/Turkish/White-European): "),

        # Jaundice options
        "jaundice": input("Enter jaundice (no/yes): ").lower(),

        # Autism options
        "austim": input("Enter autism (no/yes): ").lower(),

        # Country options (full list of countries in the encoder)
        "contry_of_res": input("Enter country of residence (e.g., United States, Vietnam, India): "),

        # Used app before options
        "used_app_before": input("Enter used app before (no/yes): ").lower(),

        # Relation options
        "relation": input("Enter relation (Others/Self): ")
    }
    return input_data


def test_prediction():
    """
    Test the autism prediction API with user input
    """
    try:
        # Get user input
        input_data = get_user_input()

        # Print input data for debugging
        print("Input Data:")
        print(json.dumps(input_data, indent=2))

        # Send POST request to prediction endpoint
        response = requests.post(
            'http://localhost:5000/api/predict',
            json=input_data,
            headers={'Content-Type': 'application/json'}
        )

        # Print the response
        print("\nResponse Status Code:", response.status_code)
        print("\nPrediction Response:")
        print(json.dumps(response.json(), indent=2))

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
    except Exception as e:
        print("Unexpected Error:", e)


if __name__ == '__main__':
    test_prediction()