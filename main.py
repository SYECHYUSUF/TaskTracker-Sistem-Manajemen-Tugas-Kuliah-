from fastapi import FastAPI
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskTracker API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "TaskTracker API Berjalan. Setup Awal Selesai."}