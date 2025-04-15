from flask import Flask, request, jsonify
from validation import validate_receipt
from utils import get_total_points
import uuid

receipts_data = {}
server = Flask(__name__)

@server.route("/")
def home():
    return "Welcome to the Fetch Rewards Receipt Processor API!"


@server.route("/receipts/<id>/points", methods=["GET"])
def get_points(id: str):
    """
    Handles GET requests to /receipts/{id}/points. 
    
    Parameters:
        id (str): The unique identifier of the receipt whose points are to be retrieved.
    
    Returns:
        JSON: A JSON response containing either the points associated with the provided 
        ID or an error message along with a corresponding HTTP status code (either 200 or 404).
    """
    
    points = receipts_data.get(id)

    if points is None:
        return jsonify(error="No receipt found for that id"), 404
        
    return jsonify(points=points)


@server.route("/receipts/process", methods=["POST"])
def process_receipts():
    """
    Handles POST requests made to /receipts/process. 
    
    Params:
        None: The function retrieves data from the request object.
    
    Returns:
        JSON: A JSON response containing either an error message (if the receipt 
        is invalid) or the unique receipt ID along with a corresponding HTTP status code.
    """
    receipt = request.get_json()
    validation_result = validate_receipt(receipt)
    
    if not validation_result.is_valid:
        return jsonify(error="The receipt is invalid", message=validation_result.message), 400
        
    receipt_id = str(uuid.uuid4())
    points = get_total_points(receipt)
    receipts_data[receipt_id] = points
    
    return jsonify(id=receipt_id), 201


if __name__ == "__main__":
   server.run(host='0.0.0.0')
