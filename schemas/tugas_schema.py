from pydantic import BaseModel
from typing import Optional

class TugasBase(BaseModel):
    judul: str
    deskripsi: Optional[str] = None
    deadline: str
    status_selesai: bool = False
    mata_kuliah_id: int

class TugasCreate(TugasBase):
    pass

class TugasResponse(TugasBase):
    id: int
    model_config = {"from_attributes": True}