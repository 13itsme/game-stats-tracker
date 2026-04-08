from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.match import MatchCreate, MatchResponse
from app.core.database import get_session
from app.crud.match import create_match, get_all_matches, get_match_by_id

router = APIRouter()


@router.post("/match", response_model=MatchResponse)
async def create_match_route(data: MatchCreate, session: AsyncSession = Depends(get_session)):
    return await create_match(session, data)

@router.get("/all_matches", response_model=list[MatchResponse])
async def get_all_matches_route(session: AsyncSession = Depends(get_session)):
    return await get_all_matches(session)

@router.get("/match/{match_id}", response_model=MatchResponse)
async def get_match_by_id_route(match_id: int, session: AsyncSession = Depends(get_session)):
    match = await get_match_by_id(session, match_id)
    if match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return match