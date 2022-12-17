from modelo_dados import Defensivos, Roupas, Gados
from conector import insere_dados_defensivos, insere_dados_roupas, insere_dados_gados
from interface import *

def adiciona_dados_defensivos():
    x = Defensivos(nome, data_entrada, quantidade_k, quantidade_l, valor_compra, data_compra)
    insere_dados_defensivos(x)


def adiciona_dados_roupas():
    y = Roupas(marca, tamanho, valor_compra, valor_venda, data_compra, cor)
    insere_dados_roupas(y)


def adiciona_dados_gados():
    z = Gados(numero, raca, tipo, peso, m_ou_f, prenha_ou_nao, parida_ou_nao, qual_pasto, numero_mae, numero_filho)
    insere_dados_gados(z)
