from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/executar")
def executar(nome: str = "usuário"):
    return {"mensagem": f"Olá, {nome}! API rodando 🚀"}