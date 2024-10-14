import requests
import json

# Dummy data for the API request
claim_data = {
    "patient_id": "PAT123",
    "service_date": "2023-07-15",
    "diagnosis_codes": ["Z79.8", "I20.1"],
    "procedure_codes": ["99203", "99215"],
    "claim_amount": 1234.56
}

base_url = "http://example.com/api/v1/"
endpoint = "claims"


def post_claim_data_to_api(claim_data):
    try:
        url = f"{base_url}{endpoint}"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, headers=headers, data=json.dumps(claim_data))

        if response.status_code == 201:
            print("Claim data sent successfully to the API.")
            return response.json()
        else:
            print(f"Failed to send claim data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error occurred during API request: {e}")
        return None


if __name__ == "__main__":
    response_data = post_claim_data_to_api(claim_data)

    if response_data:
        print("Received response data from the API:")
        print(json.dumps(response_data, indent=2))
