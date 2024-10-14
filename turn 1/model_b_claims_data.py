
from flask import Flask, request, jsonify
app = Flask(__name__)

# Dummy database of claims data
claims_data = [
    {
        "claim_id": 1,
        "patient_id": "PAT123",
        "service_date": "2021-01-01",
        "diagnosis": "Appendicitis",
        "amount": 1200.00
    },
    {
        "claim_id": 2,
        "patient_id": "PAT456",
        "service_date": "2021-06-15",
        "diagnosis": "Fractured Arm",
        "amount": 3500.00
    }
]

@app.route('/api/claims', methods=['GET'])
def get_claims():
    return jsonify(claims_data)

@app.route('/api/claims/<int:claim_id>', methods=['GET'])
def get_claim_by_id(claim_id):
    for claim in claims_data:
        if claim['claim_id'] == claim_id:
            return jsonify(claim)
    return jsonify({"message": "Claim not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
