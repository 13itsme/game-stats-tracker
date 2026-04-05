from sqlalchemy.ext.asyncio import AsyncSession
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
