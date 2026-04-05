from pydantic import BaseModel
from datetime import datetime

class MatchCreate(BaseModel):
    map_name: str
    played_at: datetime
    duration_seconds: int

class MatchResponse(BaseModel):
    id: int
    played_at: datetime
    map_name: str
    duration_seconds: int