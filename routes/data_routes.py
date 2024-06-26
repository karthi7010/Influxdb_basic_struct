import json

from fastapi import APIRouter, HTTPException
from crud.data_crud import write,get_datas

router = APIRouter()

@router.post("/data/")
async def route_create_data():
    measurement = "sensor_data"
    tags = {"Patchid": "Patch2"}
    fields = [{
        "Seq":   "1",
        "ECG0":  json.dumps([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, -3, 2, -5, 4, -29, -16, 52, 89, -126, -140, -20, 32, 98, -38, -72, -32, 31, 64, 10, -16, -25, 16, 51, 31, 1, -16, 10, 45, 41, 10, -19, 1, 48, 22, 5, -33, -18, 31, 22, -14, -41, -10, 34, 19, -3, -34, -1, 32]),
        "ECG1":  json.dumps([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, -3, 2, -5, 8, -42, -140, 8, -33, 3, -162, -151, 34, -31, -2, -50, -99, 23, -6, -2, -16, -40, 35, 17, 15, 4, -6, 44, 31, 20, 2, 6, 38, 22, 15, -10, -3, 19, 4, -4, -17, -6, 15, 4, -6, -16, 2, 16, 3, -8]),
        "Accel": json.dumps([7, 0, 220, 164, 16748, 224, 164, 16760, 220, 164, 16764, 228, 172, 16764, 220, 164, 16772, 224, 156, 16764, 228, 164, 16780, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    }]
    new_data = write(measurement, tags, fields)
    return new_data


@router.get("/data/")
async def read_data(query: str):
    pass

@router.get("/datas")
async def route_get_datas():
    try:
        # Retrieve data from InfluxDB
        data = get_datas()
        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))