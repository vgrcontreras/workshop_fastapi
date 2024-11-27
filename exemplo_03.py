from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/outro_recurso')
def pegar_recurso():
    return {'outro': 'recurso'}


@app.post('/outro_recurso/{id}')
def criar_recurso():
    return {"message": id}