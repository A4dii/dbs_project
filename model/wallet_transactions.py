from sqlalchemy import Column, Integer, ForeignKey, Float, Enum, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlModel import Base

class WalletTransaction(Base):
    __tablename__ = 'wallet_transactions'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    transaction_type = Column(Enum('deposit', 'withdrawal'), nullable=False)
    description = Column(Text)
    transaction_date = Column(DateTime, nullable=False, default=func.now())

    user = relationship("User")

    def __repr__(self):
        return f"<WalletTransaction(user_id={self.user_id}, amount={self.amount}, transaction_type={self.transaction_type}, transaction_date={self.transaction_date})>"
