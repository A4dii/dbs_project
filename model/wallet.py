from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship
from . import Base

class Wallet(Base):
    __tablename__ = 'wallets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    balance = Column(Float, nullable=False)
    currency = Column(String, nullable=False)

    user = relationship("User")

    def __repr__(self):
        return f"<Wallet(user_id={self.user_id}, balance={self.balance}, currency={self.currency})>"
