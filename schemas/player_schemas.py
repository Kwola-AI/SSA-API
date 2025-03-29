from pydantic import BaseModel
from datetime import date

class PlayerBase(BaseModel):
    player_name: str
    dob: date
    father_name: str
    mother_name: str
    father_phone: str
    mother_phone: str
    is_active: bool = True

class PlayerCreate(PlayerBase):
    pass

class PlayerUpdate(BaseModel):
    player_name: str | None = None
    dob: date | None = None
    father_name: str | None = None
    mother_name: str | None = None
    father_phone: str | None = None
    mother_phone: str | None = None
    is_active: bool | None = None

class PlayerResponse(PlayerBase):
    id: int

    class Config:
        from_attributes = True
