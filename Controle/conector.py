
from modelo_dados import *
from tinydb import TinyDB


banco_de_dados_defensivos = TinyDB("banco_de_dados_defensivos.jason")


nome = "glifosato"
quantidade_produto = "2"
data_entrada = "15/12/2022"
quantidade_k = "24"
quantidade_l = "22"

def adiciona_defensivo():
    x = Defensivos(nome, quantidade_produto, data_entrada, quantidade_k, quantidade_l)
    banco_de_dados_defensivos.append(x)
