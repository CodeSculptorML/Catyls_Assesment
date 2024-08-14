from flask import Flask, jsonify

app = Flask(__name__)

# Mock data to simulate external service data retrieval
mock_data = {
    "orders": [
        {"id": 1, "product": "Laptop", "price": 999.99},
        {"id": 2, "product": "Smartphone", "price": 499.99},
        {"id": 3, "product": "Tablet", "price": 299.99}
    ]
}

# In-memory storage for processed data
processed_data = {}


# API Endpoint to fetch and process data
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    global processed_data
    # Simulate data processing (e.g., converting product names to uppercase)
    processed_data = {order['id']: order['product'].upper() for order in mock_data['orders']}
    return jsonify({"message": "Data fetched and processed successfully"})


# API Endpoint to retrieve processed data
@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    return jsonify(processed_data)


if __name__ == '__main__':
    app.run(debug=True)