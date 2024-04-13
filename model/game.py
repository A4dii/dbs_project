from sqlalchemy import Column, Integer, String, Float, Boolean
from . import Base

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    description = Column(String)
    price = Column(Float, nullable=False)
    available = Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Game(id={self.id}, title={self.title}, price={self.price}, available={self.available})>"
