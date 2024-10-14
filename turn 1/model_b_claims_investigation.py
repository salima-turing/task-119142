import requests

BASE_URL = 'http://localhost:5000/api/claims'  # Replace this with the actual API URL


def get_all_claims():
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch claims data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return None


def get_claim_by_id(claim_id):
    url = f'{BASE_URL}/{claim_id}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Claim with ID {claim_id} not found.")
            return None
        else:
            print(f"Failed to fetch claim data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return None


if __name__ == '__main__':
    # Example usage:
    print("**Retrieving all Claims:**")
    all_claims = get_all_claims()
    if all_claims:
        for claim in all_claims:
            print(f"Claim ID: {claim['claim_id']}, Patient ID: {claim['patient_id']}")
            claim_id_to_find = 2
            print("\n**Retrieving Claim by ID:**")
            claim_data = get_claim_by_id(claim_id_to_find)
            if claim_data:
                print(claim_data)
