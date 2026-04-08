from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.players import Player
from app.schemas.player import PlayerCreate, PlayerResponse


async def create_player(session: AsyncSession, data: PlayerCreate):
    player = Player(username=data.username,
                    email=data.email)
    session.add(player)
    await session.commit()
    await session.refresh(player)
    return player

async def get_all_players(session: AsyncSession):
    result = await session.execute(select(Player))
    return result.scalars().all()

async def get_player_by_id(session: AsyncSession, player_id: int):
    result = await session.execute(select(Player).where(Player.id == player_id))
    return result.scalars().first()