from pydantic import BaseModel, EmailStr

# Модель для запроса токена
class TokenRequest(BaseModel):
    email: EmailStr

# Модель ответа с токеном
class TokenResponse(BaseModel):
    access_token: str
    token_type: str