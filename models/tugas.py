from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Tugas(Base):
    __tablename__ = "tugas"
    id = Column(Integer, primary_key=True, index=True)
    judul = Column(String, index=True)
    deskripsi = Column(String)
    deadline = Column(String)
    status_selesai = Column(Boolean, default=False)
    mata_kuliah_id = Column(Integer, ForeignKey("mata_kuliah.id"))
    mata_kuliah = relationship("MataKuliah", back_populates="tugas")