from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from app.schemas.match_result import MatchResultCreate, MatchResultResponse
from app.crud.match_result import match_result_create
from app.core.database import get_session

router = APIRouter()


@router.post("/match_result", response_model=MatchResultResponse)
async def create_match_result_route(data: MatchResultCreate, session: AsyncSession = Depends(get_session)):
    return await match_result_create(session, data)
