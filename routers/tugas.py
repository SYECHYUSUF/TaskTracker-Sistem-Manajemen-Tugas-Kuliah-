from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.tugas import Tugas
from models.mata_kuliah import MataKuliah
from schemas.tugas_schema import TugasCreate, TugasResponse
from auth.jwt_handler import get_current_user

router = APIRouter(prefix="/tugas", tags=["Tugas"])

@router.get("/", response_model=list[TugasResponse])
def get_all_tugas(db: Session = Depends(get_db)):
    return db.query(Tugas).all()

@router.post("/", response_model=TugasResponse, status_code=status.HTTP_201_CREATED)
def create_tugas(tugas: TugasCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # Dilindungi JWT (Membutuhkan token)
    mk = db.query(MataKuliah).filter(MataKuliah.id == tugas.mata_kuliah_id).first()
    if not mk:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID Mata Kuliah tidak valid")

    new_tugas = Tugas(**tugas.model_dump())
    db.add(new_tugas)
    db.commit()
    db.refresh(new_tugas)
    return new_tugas

@router.put("/{tugas_id}", response_model=TugasResponse)
def update_status_tugas(tugas_id: int, status_selesai: bool, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # Dilindungi JWT (Membutuhkan token)
    tugas = db.query(Tugas).filter(Tugas.id == tugas_id).first()
    if not tugas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tugas tidak ditemukan")
    
    tugas.status_selesai = status_selesai
    db.commit()
    db.refresh(tugas)
    return tugas