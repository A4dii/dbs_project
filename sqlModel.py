from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

from sqlalchemy import Column, Integer, ForeignKey, Float, String, Enum, Text, DateTime, Boolean, ForeignKeyConstraint
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)

    transactions = relationship("WalletTransaction", back_populates="user")

class Wallet(Base):
    __tablename__ = 'wallets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    balance = Column(Float, nullable=False)
    currency = Column(String(3), nullable=False)

    user = relationship("User")

class WalletTransaction(Base):
    __tablename__ = 'wallet_transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    transaction_type = Column(Enum('deposit', 'withdrawal'), nullable=False)
    description = Column(Text)
    transaction_date = Column(DateTime, nullable=False, default=datetime.utcnow())

    user = relationship("User", back_populates="transactions")

class UserLibrary(Base):
    __tablename__ = 'user_library'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)

    user = relationship("User")
    game = relationship("Game")

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    description = Column(String)
    price = Column(Float, nullable=False)
    available = Column(Boolean, nullable=False, default=True)

class Friendship(Base):
    __tablename__ = 'friendships'

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
