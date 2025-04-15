# Fetch Rewards Receipt Processor

# About this project 
This is a web service to process receipts as outlined [here](https://github.com/fetch-rewards/receipt-processor-challenge).


## API Specification

Endpoint: Process Receipts

- Path: /receipts/process
- Method: POST
- Payload: Receipt JSON
- Response: JSON containing an id for the receipt.

Example Response:
```
{ "id": "7fb1377b-b223-49d9-a31a-5a02701dd310" }
```

Endpoint: Get Points

- Path: /receipts/{id}/points
- Method: GET
- Response: A JSON object containing the number of points awarded.


Example Response:
```
{ "points": 32 }
```

## Tech Stack
- Python, Flask, Containerization.

## Structure

- **requirements.txt**: lists all the necessary Python packages and their versions required to run the Flask application.

- **Dockerfile**: defines the setup for a Docker container to host the Flask application.

- **src folder**:

  **server.py**: establishes a Flask web server and defines two routes to process receipts and retrieve points associated with a receipt. It imports necessary functions from utils.py and validations.py to calculate points based on receipt data and validate receipt structures, respectively. The file contains main functionality to receive POST requests at /receipts/process to process new receipts, and GET requests at /receipts/{id}/points to retrieve points associated with a given receipt ID.

  **validation.py** : contains functions to validate the receipt structure and its content, ensuring that the data provided adheres to specified conditions. For example, it checks the type and format of the retailer name, purchase date and time, total amount, and item structure in the receipt. It also defines a ValidationResult class to encapsulate the result of a validation check.

  **utils.py**: contains a collection of functions to calculate points based on different criteria provided in a receipt. Each function takes a receipt dictionary as input and returns points based on certain conditions like the retailer's name, purchase date and time, total amount, and item descriptions among others. The file also contains a main function get_total_receipt_points which aggregates points from all the criteria.

## Setup and running instructions

1. Prerequisites:

- Ensure that you have [Docker](https://www.docker.com/) installed on your machine.
- Clone the project repository.

2.Build Docker Image:

- Navigate to the project directory where the Dockerfile and requirements.txt are located.
- Run the following command to build the Docker image:

```
docker build -t my-receipts-app .
```

3. Run Docker Container:

- Once the image is built, run the following command to start the container:

```
docker run -d -p 8080:5000 my-receipts-app
```

4. Accessing the Application:

- The application will now be running in a Docker container and is accessible at http://localhost:8080.
- You can now use the defined routes to process receipts and retrieve points: http://localhost:8080/receipts/process for processing receipts and http://localhost:8080/receipts/{id}/points for retrieving points. 

curl -X POST http://localhost:8080/receipts/process \
  -H "Content-Type: application/json" \
  -d '{"retailer":"M&M Corner Market","purchaseDate":"2022-03-20","purchaseTime":"14:33","items":[{"shortDescription":"Gatorade","price":"2.25"},{"shortDescription":"Gatorade","price":"2.25"},{"shortDescription":"Gatorade","price":"2.25"},{"shortDescription":"Gatorade","price":"2.25"}],"total":"9.00"}'
  
curl http://localhost:8080/receipts/{receipt_id}/points



5. Stop and Remove Docker Container:

- To stop the running container, first find the container ID with the following command:

```
docker ps
```

Then stop the container with:

```
docker stop <container-id>
```
