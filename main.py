# main.py
import logging
from fastapi import FastAPI
from models import AdditionRequest, AdditionResponse
from controllers import add_numbers_in_batches
from datetime import datetime

logging.basicConfig(filename='app.log', level=logging.INFO)


app = FastAPI()

@app.post("/addition", response_model=AdditionResponse)
async def addition(request: AdditionRequest):
    response_data = {
        "batchid": request.batchid,
        "response": add_numbers_in_batches(request),
        "status": "complete",
        "started_at": datetime.now().isoformat(),
        "completed_at": datetime.now().isoformat()
    }
    return response_data

