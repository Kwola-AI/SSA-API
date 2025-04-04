from sqlalchemy import Column, Integer, String, Boolean, Date

from .database import Base  # Update this import


class PlayerDetails(Base):
    __tablename__ = "player_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    player_name = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    father_name = Column(String, nullable=False)
    mother_name = Column(String, nullable=False)
    father_phone = Column(String, nullable=False)
    mother_phone = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
