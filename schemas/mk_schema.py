from pydantic import BaseModel, Field

class MkBase(BaseModel):
    kode_mk: str
    nama_mk: str
    sks: int = Field(gt=0)

class MkCreate(MkBase):
    pass

class MkResponse(MkBase):
    id: int
    model_config = {"from_attributes": True}