from modelo_dados import *
from tinydb import TinyDB


banco_de_dados_defensivos = TinyDB("banco_de_dados_defensivos.json")
banco_de_dados_roupas = TinyDB("banco_de_dados_roupas.json")
banco_de_dados_gados = TinyDB("banco_de_dados_gados.json")


def insere_dados_defensivos(modelo_dados: Defensivos):
    banco_de_dados_defensivos.insert({
    "nome": modelo_dados.nome,
    "quantidade_produto": modelo_dados.quantidade_produto,
    "preco": modelo_dados.preco,
    "data_entrada": modelo_dados.data_entrada,
    "quantidade_k": modelo_dados.quantidade_k,
    "quantidade_l": modelo_dados.quantidade_l
    })

def insere_dados_roupas(modelo_dados: Roupas):
    banco_de_dados_roupas.insert({
    "marca": modelo_dados.marca,
    "tamanho": modelo_dados.tamanho,
    "valor_compra": modelo_dados.valor_compra,
    "valor_venda": modelo_dados.valor_venda,
    "data_compra": modelo_dados.data_compra,
    "cor": modelo_dados.cor
    })

def insere_dados_gados(modelo_dados: Gados):
    banco_de_dados_gados.insert({
    "numero": modelo_dados.numero,
    "raca": modelo_dados.raca,
    "tipo": modelo_dados.tipo,
    "peso": modelo_dados.peso,
    "m_ou_f": modelo_dados.m_ou_f,
    "prenha_ou_nao": modelo_dados.prenha_ou_nao,
    "parida_ou_nao": modelo_dados.parida_ou_nao,
    "qual_pasto": modelo_dados.qual_pasto
    })
