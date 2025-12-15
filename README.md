# Dockerized FastAPI Microservice

A production-style REST API built with FastAPI and containerized using Docker.
The service demonstrates environment-based configuration, health checks, and logging, and is designed to be cloud and Kubernetes ready

## Features
- REST API using FastAPI
- Dockerized application
- Environment variable configuration
- Health check endpoint
- Structured logging

## Endpoints
- '/' - Service info
- '/health' - Health check
- '/config' - Environment configuration
- '/items/{id}' - Sample business endpoint
- '/logs-demo' - Generates logs

## Build and Run

```bash
docker build -t docker-microservice .
docker run -d -p 8000:8000 docker-microservice
```

## Run the Container

```bash
docker run -d \
  -p 8000:8000 \
  -e SERVICE_NAME=inventory-api \
  -e ENVIRONMENT=local \
  docker-microservice
```

## Technologies Used
- Python
- FastAPI
- Docker
