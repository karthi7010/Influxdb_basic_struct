from fastapi import FastAPI
from routes import data_routes

app = FastAPI()

app.include_router(data_routes.router, prefix="/api")
