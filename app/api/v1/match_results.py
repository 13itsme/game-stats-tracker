from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.match_result import MatchResultCreate, MatchResultResponse
from app.crud.match_result import match_result_create, get_all_match_results, get_match_results_by_id
from app.core.database import get_session

router = APIRouter()


@router.post("/match_result", response_model=MatchResultResponse)
async def create_match_result_route(data: MatchResultCreate, session: AsyncSession = Depends(get_session)):
    return await match_result_create(session, data)

@router.get("/all_match_results", response_model=list[MatchResultResponse])
async def get_all_match_results_route(session: AsyncSession = Depends(get_session)):
    return await get_all_match_results(session)

@router.get("/match_results/{match_result_id}", response_model=MatchResultResponse)
async def get_match_results_by_id_route(match_result_id: int, session: AsyncSession = Depends(get_session)):
    match_results = await get_match_results_by_id(session, match_result_id)
    if match_results is None:
        raise HTTPException(status_code=404, detail="Match results not found")
    return match_results