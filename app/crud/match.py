from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.matches import Matches
from app.schemas.match import MatchCreate, MatchResponse

async def create_match(session: AsyncSession, data: MatchCreate):
    match = Matches(map_name=data.map_name,
                    played_at=data.played_at,
                    duration_seconds=data.duration_seconds)
    session.add(match)
    await session.commit()
    await session.refresh(match)
    return match

async def get_all_matches(session: AsyncSession):
    result = await session.execute(select(Matches))
    return result.scalars().all()

async def get_match_by_id(session: AsyncSession, match_id: int):
    result = await session.execute(select(Matches).where(Matches.id == match_id))
    return result.scalars().first()