from pydantic import BaseModel
from datetime import datetime


class PlayerCreate(BaseModel):
    username: str
    email: str


class PlayerResponse(BaseModel):
    id: int
    username: str
    email: str
    registered_at: datetime