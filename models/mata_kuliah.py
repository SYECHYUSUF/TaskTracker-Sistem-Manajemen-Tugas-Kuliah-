from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class MataKuliah(Base):
    __tablename__ = "mata_kuliah"
    id = Column(Integer, primary_key=True, index=True)
    kode_mk = Column(String, unique=True, index=True)
    nama_mk = Column(String)
    sks = Column(Integer)
    tugas = relationship("Tugas", back_populates="mata_kuliah", cascade="all, delete-orphan")