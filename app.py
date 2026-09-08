from fastapi import FastAPI
from pydantic import BaseModel
from typing import List  # <-- Import List tracking

app = FastAPI()

class SerialData(BaseModel):
    timestamp: str
    value: str

@app.post("/api/soil/bulk")
async def receive_bulk_soil_data(data_list: List[SerialData]):
    print(f" Received Bulk Soil Data Contains {len(data_list)} messages.")
    for item in data_list:
        if(int(item.value) <=550):
            print("Soil Moisture Value is below threshold of 550!")
        
    return {"status": "success", "processed_items": len(data_list)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8069)
