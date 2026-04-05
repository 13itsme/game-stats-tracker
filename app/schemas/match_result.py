from pydantic import BaseModel

class MatchResultCreate(BaseModel):
    player_id: int
    match_id: int
    kills: int
    deaths: int
    assists: int
    winner: bool

class MatchResultResponse(BaseModel):
    id: int
    player_id: int
    match_id: int
    kills: int
    deaths: int
    assists: int
    winner: bool