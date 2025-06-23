from pydantic import BaseModel

# Модель для запроса токена
class TokenRequest(BaseModel):
    email: str

# Модель ответа с токеном
class TokenResponse(BaseModel):
    access_token: str
    token_type: str