import joblib

modelo = joblib.load(filename='modelo_casas.pkl')

def prever_preco(
    tamanho: int,
    quartos: int,
    nr_vagas: int,
):
    dados_entrada = [[tamanho, quartos, nr_vagas]]
    preco_estimado = modelo.predict(dados_entrada)[0]

    return round(preco_estimado, 2)

print(prever_preco(300, 3, 2))