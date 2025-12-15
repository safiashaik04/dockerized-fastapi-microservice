import os
import logging
from fastapi import FastAPI

app = FastAPI(title="Containerized Microservice")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("microservice")

SERVICE_NAME = os.getenv("SERVICE_NAME", "inventory-service")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {
        "service": SERVICE_NAME,
        "environment": ENVIRONMENT,
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/config")
def config():
    return {
        "service_name": SERVICE_NAME,
        "environment": ENVIRONMENT
    }

@app.get("/items/{item_id}")
def get_item(item_id: int):
    logger.info(f"Fetching item with ID {item_id}")
    return {
        "item_id": item_id,
        "name": f"Item-{item_id}",
        "price": item_id * 10.0
    }

@app.get("/logs-demo")
def logs_demo():
    logger.warning("This is a warning log")
    logger.error("This is an error log")
    return {"message": "Logs have been generated successfully"}

