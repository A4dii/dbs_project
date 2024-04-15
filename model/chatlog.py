from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlModel import Base

class ChatLog(Base):
    __tablename__ = 'chatlogs'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    message = Column(String, nullable=False)
    sent_at = Column(DateTime, nullable=False)

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])

    def __repr__(self):
        return f"<ChatLog(sender_id={self.sender_id}, receiver_id={self.receiver_id}, message={self.message}, sent_at={self.sent_at})>"
