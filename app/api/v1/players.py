from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.player import PlayerCreate, PlayerResponse
from app.core.database import get_session
from app.crud.player import create_player

router = APIRouter()


@router.post("/player", response_model=PlayerResponse)
async def create_player_route(data: PlayerCreate, session: AsyncSession = Depends(get_session)):
    return await create_player(session, data)
