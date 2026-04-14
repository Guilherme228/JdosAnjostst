from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from firebase_config import auth
from schemas import LoginRequest, CadastroRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/cadastro")
def cadastro(request: CadastroRequest):
    try:
        auth.create_user_with_email_and_password(
            request.email,
            request.senha
        )
        return {"mensagem": "Usuário criado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Email já cadastrado ou senha fraca")

@app.post("/login")
def login(request: LoginRequest):
    try:
        usuario = auth.sign_in_with_email_and_password(
            request.email,
            request.senha
        )
        return {
            "token": usuario["idToken"],
            "email": usuario["email"]
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")