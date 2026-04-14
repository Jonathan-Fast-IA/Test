from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Simulação de banco em memória
usuarios = []

# Modelo de entrada
class Usuario(BaseModel):
    nome: str
    idade: int
    email: str

@app.get("/")
def home():
    return {
        "status": "online",
        "sistema": "API de testes",
        "horario": datetime.now().isoformat()
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "mensagem": "API funcionando corretamente"
    }

@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    usuarios.append(usuario.dict())
    return {
        "mensagem": "Usuário criado com sucesso",
        "total_usuarios": len(usuarios),
        "dados": usuario
    }

@app.get("/usuarios")
def listar_usuarios():
    return {
        "total": len(usuarios),
        "usuarios": usuarios
    }

@app.get("/executar")
def executar(nome: str, tarefa: str = "processar dados"):
    return {
        "mensagem": f"Olá {nome}, tarefa '{tarefa}' executada com sucesso",
        "status": "concluído",
        "timestamp": datetime.now().isoformat()
    }