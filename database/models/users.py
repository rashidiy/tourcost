from typing import Union

from sqlalchemy import Column, Integer, BigInteger, String, Enum, select

from database.database import Base, db, TableBase


class User(Base, TableBase):
    user_id: int = Column(BigInteger, nullable=False, unique=True)
    full_name: str = Column(String(255), nullable=True)
    phone: Union[str, None] = Column(String(15), nullable=True)
    language: str = Column(Enum('uz', 'ru'), nullable=True)

    @classmethod
    async def get_by_user_id(cls, user_id):
        query = select(cls).where(cls.user_id == user_id)
        users = await db.execute(query)
        user, = users.first() or (None,)
        return user
