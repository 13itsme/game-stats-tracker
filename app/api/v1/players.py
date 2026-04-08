from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.player import PlayerCreate, PlayerResponse
from app.core.database import get_session
from app.crud.player import create_player, get_all_players, get_player_by_id


router = APIRouter()


@router.post("/player", response_model=PlayerResponse)
async def create_player_route(data: PlayerCreate, session: AsyncSession = Depends(get_session)):
    return await create_player(session, data)

@router.get("/all_player", response_model=list[PlayerResponse])
async def get_all_player_route(session: AsyncSession = Depends(get_session)):
    return await get_all_players(session)

@router.get("/player/{player_id}", response_model=PlayerResponse)
async def get_player_by_id_route(player_id: int, session: AsyncSession = Depends(get_session)):
    player = await get_player_by_id(session, player_id)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player