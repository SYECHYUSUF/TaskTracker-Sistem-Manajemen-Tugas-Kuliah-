from fastapi import FastAPI
from database import engine, Base
from routers import auth, mata_kuliah, tugas

# Import models agar tabel terbuat di database
import models.user
import models.mata_kuliah
import models.tugas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TaskTracker API",
    description="API Manajemen Tugas Kuliah untuk UTS Pemrograman Web Lanjutan",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(mata_kuliah.router)
app.include_router(tugas.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Selamat datang di TaskTracker API. Buka /docs untuk dokumentasi."}