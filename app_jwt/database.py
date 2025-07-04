from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    "sqlite+aiosqlite:///test.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class User(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: str
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]

# Функция создания таблиц
async def create_tabels():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

# Функция удаления таблиц
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)