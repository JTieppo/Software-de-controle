from modelo_dados import Defensivos, Roupas, Gados
from conector import insere_dados_defensivos, insere_dados_roupas, insere_dados_gados
from interface import *

def adiciona_dados_defensivos():
    nome = interface_defensivos.nome
    data_entrada = interface_defensivos.data_entrada
    quantidade_k = interface_defensivos.quantidade_k
    quantidade_l = interface_defensivos.quantidade_l
    valor_compra = interface_defensivos.valor_compra
    data_compra = interface_defensivos.data_compra

    x = Defensivos(nome, data_entrada, quantidade_k, quantidade_l, valor_compra, data_compra)
    insere_dados_defensivos(x)


def adiciona_dados_roupas():
    marca = interface_roupas.marca
    tamanho = interface_roupas.tamanho
    valor_compra = interface_roupas.valor_compra
    valor_venda = interface_roupas.valor_venda
    data_compra = interface_roupas.data_compra
    cor = interface_roupas.cor

    y = Roupas(marca, tamanho, valor_compra, valor_venda, data_compra, cor)
    insere_dados_roupas(y)


def adiciona_dados_gados():
    numero = interface_gados.numero
    raca = interface_gados.raca
    tipo = interface_gados.tipo
    peso = interface_gados.peso
    m_ou_f = interface_gados.m_ou_f
    prenha_ou_nao = interface_gados.prenha_ou_nao
    parida_ou_nao = interface_gados.parida_ou_nao
    pasto = interface_gados.pasto

    z = Gados(numero, raca, tipo, peso, m_ou_f, prenha_ou_nao, parida_ou_nao, pasto)
    insere_dados_gados(z)
