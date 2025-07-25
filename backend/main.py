from fastapi import FastAPI
from database import create_db_and_tables
from feeds import router as feeds_router

app = FastAPI()

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(feeds_router)