from fastapi import FastAPI

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
    if("esp" not in services):
        return {"clean_host": "","port": 0}   
    return {"clean_host": services["esp"],"port": 443}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
