from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# ---- MODELO GENÉRICO ----
class Request(BaseModel):
    operacao: str
    a: Optional[float] = None
    b: Optional[float] = None
    valor: Optional[float] = None

# ---- LÓGICA CENTRAL ----
@app.post("/processar")
def processar(req: Request):

    op = req.operacao.lower()

    # 🧮 CALCULADORA
    if op == "somar":
        return {"resultado": req.a + req.b}

    elif op == "subtrair":
        return {"resultado": req.a - req.b}

    elif op == "multiplicar":
        return {"resultado": req.a * req.b}

    elif op == "dividir":
        if req.b == 0:
            return {"erro": "divisão por zero"}
        return {"resultado": req.a / req.b}

    # 💰 IMPOSTO
    elif op == "imposto":
        if req.valor <= 2000:
            taxa = 0
        elif req.valor <= 5000:
            taxa = 0.1
        elif req.valor <= 10000:
            taxa = 0.2
        else:
            taxa = 0.3

        imposto = req.valor * taxa

        return {
            "valor": req.valor,
            "taxa": taxa,
            "imposto": imposto,
            "liquido": req.valor - imposto
        }

    # ❌ OPERAÇÃO INVÁLIDA
    return {"erro": "operação inválida"}