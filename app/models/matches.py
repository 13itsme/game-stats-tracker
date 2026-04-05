from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from datetime import datetime


class Matches(Base):
    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(primary_key=True)
    played_at: Mapped[datetime]
    map_name: Mapped[str]
    duration_seconds: Mapped[int]
