import joblib
from fastapi import FastAPI
from pydantic import BaseModel


class PreverPrecoRequest(BaseModel):
    tamanho: int
    quartos: int
    nr_vagas: int

class PreverPrecoResponse(BaseModel):
    preco: float

modelo = joblib.load(filename='modelo_casas.pkl')

app = FastAPI()

@app.post('/', response_model=PreverPrecoResponse)
def prever_preco(
    orcamento: PreverPrecoRequest
):
    dados_entrada = [[orcamento.tamanho, orcamento.quartos, orcamento.nr_vagas]]
    preco_estimado = modelo.predict(dados_entrada)[0]

    return {'preco': round(preco_estimado, 2)}
