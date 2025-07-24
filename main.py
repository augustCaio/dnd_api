from fastapi import FastAPI
from routes.races import router as races_router

app = FastAPI()

app.include_router(races_router) 