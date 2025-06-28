from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import delete_tables, create_tabels
from token_jwt.routers.token import router as token_router

# Фукция для логгирования (удобно во время тестов, что база очищается при каждом тесте)
@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tabels()
    print("База готова к работе")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(token_router)