from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Membership(Base):
    __tablename__ = 'memberships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    community_id = Column(Integer, ForeignKey('communities.id'), nullable=False)

    user = relationship("User")
    community = relationship("Community")

    def __repr__(self):
        return f"<Membership(user_id={self.user_id}, community_id={self.community_id})>"
