from sqlalchemy import Column, Integer, String
from . import Base

class GameShop(Base):
    __tablename__ = 'game_shops'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)

    def __repr__(self):
        return f"<GameShop(id={self.id}, name={self.name})>"
