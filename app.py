from fastapi import FastAPI, Query
from urllib.parse import urlparse
import uvicorn

app = FastAPI()

services = {}

def extract_clean_host(raw_url: str) -> str:
    """Strips https://, http://, ports, and trailing slashes from a URL."""
    raw_url = raw_url.strip()
    if not raw_url.startswith(("http://", "https://")):
        raw_url = "https://" + raw_url
    
    parsed = urlparse(raw_url)
    return parsed.hostname or raw_url

@app.get("/")
async def root():
    return {"message": "Welcome to the IoT Routing API"}

# Accepts query params: /push?service=esp&url=https://a1b2c3d4.pinggy.link/
@app.get("/push")
async def push_service(service: str, url: str):
    clean_host = extract_clean_host(url)
    services[service] = clean_host
    return {
        "message": "Service URL updated successfully",
        "service": service,
        "raw_url": url,
        "clean_host": clean_host
    }

@app.get("/getESPService")
async def get_service():
    if "esp" not in services or not services["esp"]:
        return {"clean_host": "", "port": 0}
    
    return {
        "clean_host": services["esp"],
        "port": 443
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)