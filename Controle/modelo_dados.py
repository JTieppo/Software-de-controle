class Defensivos:
    def __init__(self, nome, quantidade_produto, data_entrada, preco, quantidade_k, quantidade_l) -> None:
        self.nome = nome
        self.quantidade_produto = quantidade_produto
        self.data_entrada = data_entrada
        self.preco = preco
        self.quantidade_k = quantidade_k
        self.quantidade_l = quantidade_l

class Roupas:
    def __init__(self, marca, tamanho, valor_compra, valor_venda, data_compra, cor) -> None:
        self.marca = marca
        self.tamanho = tamanho
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.data_compra = data_compra
        self.cor = cor
        

class Gados:
    def __init__(self, numero, raca, tipo, peso, m_ou_f, prenha_ou_nao, parida_ou_nao, qual_pasto) -> None:
        self.numero = numero
        self.raca = raca
        self.tipo = tipo
        self.peso = peso
        self.m_ou_f = m_ou_f
        self.prenha_ou_nao = prenha_ou_nao
        self.parida_ou_nao = parida_ou_nao
        self.qual_pasto = qual_pasto
