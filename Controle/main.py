from conector import *


nome = "glifosato"
quantidade_produto = "2"
preco = "2000"
data_entrada = "15/12/2022"
quantidade_k = "24"
quantidade_l = "22"

def adiciona_dados_defensivos():
    x = Defensivos(nome, quantidade_produto, data_entrada, preco, quantidade_k, quantidade_l)
    insere_dados_defensivos(x)
adiciona_dados_defensivos()
