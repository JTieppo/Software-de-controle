from modelo_dados import *
from tinydb import TinyDB


banco_de_dados_defensivos = TinyDB("banco_de_dados_defensivos.json")


def insere_dados_defensivos(modelo_dados: Defensivos):
    banco_de_dados_defensivos.insert({
    "nome": modelo_dados.nome,
    "quantidade_produto": modelo_dados.quantidade_produto,
    "preco": modelo_dados.preco,
    "data_entrada": modelo_dados.data_entrada,
    "quantidade_k": modelo_dados.quantidade_k,
    "quantidade_l": modelo_dados.quantidade_l
    })
    
