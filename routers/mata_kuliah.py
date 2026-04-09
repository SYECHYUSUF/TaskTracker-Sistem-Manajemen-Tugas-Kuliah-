from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.mata_kuliah import MataKuliah
from schemas.mk_schema import MkCreate, MkResponse
from auth.jwt_handler import get_current_user

router = APIRouter(prefix="/mata-kuliah", tags=["Mata Kuliah"])

@router.get("/", response_model=list[MkResponse])
def get_all_mk(db: Session = Depends(get_db)):
    return db.query(MataKuliah).all()

@router.post("/", response_model=MkResponse, status_code=status.HTTP_201_CREATED)
def create_mk(mk: MkCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # Dilindungi JWT (Membutuhkan token)
    db_mk = db.query(MataKuliah).filter(MataKuliah.kode_mk == mk.kode_mk).first()
    if db_mk:
        raise HTTPException(status_code=400, detail="Kode MK sudah ada")
    
    new_mk = MataKuliah(**mk.model_dump())
    db.add(new_mk)
    db.commit()
    db.refresh(new_mk)
    return new_mk

@router.delete("/{mk_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_mk(mk_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # Dilindungi JWT (Membutuhkan token)
    mk = db.query(MataKuliah).filter(MataKuliah.id == mk_id).first()
    if not mk:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mata Kuliah tidak ditemukan")
    
    db.delete(mk)
    db.commit()
    return {"message": "Mata Kuliah berhasil dihapus"}