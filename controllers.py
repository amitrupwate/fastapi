# controllers.py
from typing import List
from multiprocessing import Pool
from datetime import datetime
import logging
from models import AdditionRequest

def perform_addition(payload: List[List[int]]) -> List[int]:
    return [sum(sublist) for sublist in payload]

def add_numbers_in_batches(request: AdditionRequest) -> List[int]:
    start_time = datetime.now().isoformat()
    logging.info(f"Batch {request.batchid} started at {start_time}")
    try:
        with Pool() as pool:
            results = pool.map(perform_addition, request.payload)
        end_time = datetime.now().isoformat()
        logging.info(f"Batch {request.batchid} completed at {end_time}")
        return results
    except Exception as e:
        logging.error(f"Error processing batch {request.batchid}: {str(e)}")
        raise
