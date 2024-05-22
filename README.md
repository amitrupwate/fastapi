# FastAPI Multiprocessing Addition Project

# Description
This project implements a FastAPI-based web service for performing addition on input lists of integers using Python's multiprocessing pool. It includes request and response validation using Pydantic models and implements appropriate error handling and logging for debugging and monitoring activities.

# Installation Instructions
1. Clone the repository to your local machine:
git clone <(https://github.com/amitrupwate/fastapi.git)>
2. Navigate to the project directory:
cd fastapi-multiprocessing-addition
3. Install dependencies:

# Usage
1. Run the FastAPI server
uvicorn main:app --reload
2. Make requests to the endpoint using tools like cURL or Postman. The endpoint accepts POST requests with the following JSON payload format:
{
    "batchid": "id0101",
    "payload": [[1, 2], [3, 4]]
}
The response format is as follows:
{
    "batchid": "id0101",
    "response": [3, 7],
    "status": "complete",
    "started_at": "<timestamp>",
    "completed_at": "<timestamp>"
}

# Project Structure
The project follows the MVC (Model-View-Controller) format with the following structure:

* app/: Contains the FastAPI application code.
* controllers/: Contains the logic for request handling.
* models/: Contains Pydantic models for request and response validation.
* services/: Contains the logic for performing addition using multiprocessing.
* tests/: Contains unit tests for all edge cases and scenarios.

# Implementation Details
The addition logic is implemented using Python's multiprocessing pool to parallelize the computation. Error handling and logging are implemented to ensure robustness and facilitate debugging and monitoring.

# Unit Tests
Unit tests are provided for all edge cases and scenarios. To run the tests, execute:
pytest

# Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

# Contact Information
For any questions or feedback, feel free to contact the project maintainer:

Name: Amit Rupwate
Email: amitrupwate.ar@gmail.com

# License
This project is licensed under the MIT License. See the LICENSE file for details.

 
