from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.match_results import MatchResult
from app.schemas.match_result import MatchResultResponse, MatchResultCreate


async def match_result_create(session: AsyncSession, data: MatchResultCreate):
    match_result = MatchResult(player_id=data.player_id,
                               match_id=data.match_id,
                               kills=data.kills,
                               deaths=data.deaths,
                               assists=data.assists,
                               winner=data.winner)
    session.add(match_result)
    await session.commit()
    await session.refresh(match_result)
    return match_result

async def get_all_match_results(session: AsyncSession):
    result = await session.execute(select(MatchResult))
    return result.scalars().all()

async def get_match_results_by_id(session: AsyncSession, match_result_id: int):
    result = await session.execute(select(MatchResult).where(MatchResult.id == match_result_id))
    return result.scalars().first()