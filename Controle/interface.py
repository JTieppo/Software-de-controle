from tkinter import *
from modelo_dados import Defensivos

def interface_defensivos():
    janela_defensivo = Tk()
    janela_defensivo.title("Controle de defensivos")

    nome = Entry()
    data_entrada = Entry()
    quantidade_k = Entry()
    quantidadde_l = Entry()
    valor_compra = Entry()
    data_compra = Entry()
    

    janela_defensivo.mainloop()


# Executa a janela para visualização de dados roupas
def interface_roupas():
    janela_roupas = Tk()
    janela_roupas.title("Controle de roupas")

    marca = Entry(janela_roupas)
    tamanho = Entry(janela_roupas)
    valor_compra = Entry(janela_roupas)
    valor_venda = Entry(janela_roupas)
    data_compra = Entry(janela_roupas)
    cor = Entry(janela_roupas)

    janela_roupas.mainloop()


# Executa a janela para visualização de dados gado
def interface_gados():
    janela_gado = Tk()
    janela_gado.title("Controle de gado")

    numero = Entry(janela_gado)
    raca = Entry(janela_gado)
    tipo = Entry(janela_gado)
    peso = Entry(janela_gado)
    m_ou_f = Entry(janela_gado)
    prenha_ou_nao = Entry(janela_gado)
    parida_ou_nao = Entry(janela_gado)
    qual_pasto = Entry(janela_gado)
    numero_mae = Entry(janela_gado)
    numero_filho = Entry(janela_gado)

    janela_gado.mainloop()


# Executa janela inicial
janela_inicial = Tk()
janela_inicial.title("Controle de dados")
janela_inicial.geometry("400x400")

botão_Defensivos = Button(janela_inicial, text="Defensivos", command=interface_defensivos)
botão_Defensivos.grid(padx=150, pady=50)

botão_Roupas = Button(janela_inicial, text="Roupas", command=interface_roupas)
botão_Roupas.grid(padx=150, pady=51)

botão_Gado = Button(janela_inicial, text="Gado", command=interface_gados)
botão_Gado.grid(padx=150, pady=52)

janela_inicial.mainloop()



