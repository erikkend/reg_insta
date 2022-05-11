from sqlalchemy import Column, VARCHAR, Integer
from .base import Base


class Account(Base):

    __tablename__ = "inst_accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(200))
    login = Column(VARCHAR(200))
    acc_password = Column(VARCHAR(200))
    session_id = Column(VARCHAR(200))
