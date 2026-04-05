from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.match import MatchCreate, MatchResponse
from app.core.database import get_session
from app.crud.match import create_match

router = APIRouter()


@router.post("/match", response_model=MatchResponse)
async def create_match_route(data: MatchCreate, session: AsyncSession = Depends(get_session)):
    return await create_match(session, data)
