# FastAPI Multiprocessing Addition Project

# Description
This project implements a FastAPI-based web service for performing addition on input lists of integers using Python's multiprocessing pool. It includes request and response validation using Pydantic models and implements appropriate error handling and logging for debugging and monitoring activities.

# Installation Instructions
1. Clone the repository to your local machine:
git clone <(https://github.com/amitrupwate/fastapi.git)>
2. Navigate to the project directory:
cd fastapi-multiprocessing-addition
3. Install dependencies:

# Usage in Assessment
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
Sure, here's how you can structure your project:

```
project_directory/
│
├── main.py
├── requirements.txt
└── app/
    ├── __init__.py
    ├── api/
    │   ├── __init__.py
    │   └── endpoints.py
    ├── models/
    │   ├── __init__.py
    │   └── payload.py
    └── utils/
        └── __init__.py
```

Explanation:

- `main.py`: This is your main application file where you initialize your FastAPI application and run the server.
- `requirements.txt`: This file contains the dependencies required for your project. You can generate it using `pip freeze > requirements.txt`.
- `app/`: This directory contains your FastAPI application code.
    - `__init__.py`: This file marks the `app` directory as a Python package.
    - `api/`: This directory contains your API endpoints.
        - `__init__.py`: This file marks the `api` directory as a Python package.
        - `endpoints.py`: This file contains the FastAPI endpoint definitions.
    - `models/`: This directory contains your Pydantic models.
        - `__init__.py`: This file marks the `models` directory as a Python package.
        - `payload.py`: This file contains the Pydantic model for the payload data.
    - `utils/`: This directory contains utility functions or modules that your application may need.
        - `__init__.py`: This file marks the `utils` directory as a Python package.

This structure helps organize your code into logical components, making it easier to manage as your project grows. Each component has its own responsibility, such as defining endpoints, models, or utility functions.


* app/: Contains the FastAPI application code.
  Got it! Here's the revised project structure with the FastAPI application code directly within the `app` directory:

```
project_directory/
│
├── main.py
├── requirements.txt
└── app/
    ├── __init__.py
    ├── endpoints.py
    ├── models.py
    └── fastapi_app.py
```

Explanation:

- `main.py`: This file remains your main application entry point where you initialize and run your FastAPI server.
- `requirements.txt`: This file contains the dependencies required for your project.
- `app/`: This directory contains your FastAPI application code.
    - `__init__.py`: This file marks the `app` directory as a Python package.
    - `endpoints.py`: This file contains the FastAPI endpoint definitions.
    - `models.py`: This file contains Pydantic models.
    - `fastapi_app.py`: This file contains the FastAPI application instance and its configurations. You define the FastAPI app object, middleware, exception handlers, etc., here.

This structure keeps all the FastAPI-related code together in the `app` directory, making it clear where to find the application logic.
* 
* controllers/: Contains the logic for request handling.
* models/: Contains Pydantic models for request and response validation.
* services/: Contains the logic for performing addition using multiprocessing.
* tests/: Contains unit tests for all edge cases and scenarios.

# fastapi_app.py
This file contains the FastAPI application instance and its configurations.
from fastapi import FastAPI
from datetime import datetime
from .endpoints import router as api_router

app = FastAPI()

# Include API endpoints defined in endpoints.py
app.include_router(api_router)

# endpoints.py
from fastapi import APIRouter, HTTPException
from datetime import datetime
from .models import Payload

router = APIRouter()

@router.post("/process/")
async def process(payload: Payload):
    # Process the payload
    response = [sum(inner_list) for inner_list in payload.payload]

    # Prepare the response
    response_data = {
        "batchid": payload.batchid,
        "response": response,
        "status": "complete",
        "started_at": datetime.now(),
        "completed_at": datetime.now()
    }

    return response_data

 # models.py
 This file contains Pydantic models.
 
 from typing import List
from pydantic import BaseModel

class Payload(BaseModel):
    batchid: str
    payload: List[List[int]]

# main.py
This file remains your main application entry point where you initialize and run your FastAPI server.

from fastapi import FastAPI
from app.fastapi_app import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
    
# requirements.txt
fastapi
uvicorn

These details outline how your FastAPI application is structured and how its components interact with each other.
    

# Contact Information
For any questions or feedback, feel free to contact the project maintainer:

Name: Amit Rupwate
Email: amitrupwate.ar@gmail.com

# License
This project is licensed under the MIT License. See the LICENSE file for details.

 
