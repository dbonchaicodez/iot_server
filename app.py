from urllib import response
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List  # <-- Import List tracking

app = FastAPI()

services = {}
@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
@app.get("/push")
async def pushService(service: str,url: str):
    if service not in services:
        services[service] = url
    else:
        services[service] = url
    return {"message": "Service URL updated successfully", "service": service, "url": url}
@app.get("/getESPService")
async def get_service():
    return {"clean_host": services["esp"],"port": 443}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
