from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Boolean, String

from retosquadmakers.data_access.database import Base


class JokeModel(Base):
    __tablename__ = "joke"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    is_delete = Column(Boolean, default=False, nullable=False)
    delete_at = Column(DateTime, nullable=True)
    joke = Column(String, nullable=False)
