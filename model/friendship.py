from sqlalchemy import Column, Integer, ForeignKey, String, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlModel import Base
from enum import Enum

class Friendship(Base):
    __tablename__ = 'friendships'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id1 = Column(Integer, nullable=False)
    user_id2 = Column(Integer, nullable=False)
    status = Column(String, nullable=True)

    __table_args__ = (
        ForeignKeyConstraint(['user_id1'], ['users.id']),
        ForeignKeyConstraint(['user_id2'], ['users.id'])
    )

    user1 = relationship("User", foreign_keys=[user_id1])
    user2 = relationship("User", foreign_keys=[user_id2])

    def __repr__(self):
        return f"<Friendship(user_id={self.user_id1}, friend_id={self.user_id2})>"
