from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    senha: str

class CadastroRequest(BaseModel):
    email: EmailStr
    senha: str