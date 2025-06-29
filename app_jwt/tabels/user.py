from sqlalchemy.orm import Mapped, mapped_column
from tabels.model import Model

class User(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: str
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]