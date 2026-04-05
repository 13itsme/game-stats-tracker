from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from datetime import datetime

class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    registered_at: Mapped[datetime] = mapped_column(default=datetime.now)