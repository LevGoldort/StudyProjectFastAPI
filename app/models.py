from sqlalchemy import Column, Integer, String

from .db import Base

# model/table
class Character(Base):
    __tablename__ = "characters"

    # fields
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    dnd_class = Column(String(20))
    level = Column(Integer)
    race = Column(String(20))
    alignment = Column(String(20))
