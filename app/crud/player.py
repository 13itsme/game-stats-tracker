from sqlalchemy.ext.asyncio import AsyncSession
from app.models.players import Player
from app.schemas.player import PlayerCreate, PlayerResponse


async def create_player(session: AsyncSession, data: PlayerCreate):
    player = Player(username=data.username,
                    email=data.email)
    session.add(player)
    await session.commit()
    await session.refresh(player)
    return player
