from sqlalchemy import Column, Integer, String
from . import Base

class Community(Base):
    __tablename__ = 'communities'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    def __repr__(self):
        return f"<Community(id={self.id}, name={self.name})>"
