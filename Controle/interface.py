from tkinter import *
from modelo_dados import Defensivos

def janela_defensivos():
    janela_defensivo = Tk()
    janela_defensivo.title("Controle de defensivos")

    Defensivos.nome = Entry()
    data_entrada = Entry(janela_defensivo)
    quantidade_k = Entry(janela_defensivo)
    quantidadde_l = Entry(janela_defensivo)
    valor_de_compra = Entry(janela_defensivo)
    data_de_compra = Entry(janela_defensivo)
    

    janela_defensivo.mainloop()


# Executa a janela para visualização de dados roupas
def janela_roupas():
    cria_janela_roupas = Tk()
    cria_janela_roupas.title("Controle de roupas")

    marca = Entry(cria_janela_roupas)
    tamanho = Entry(cria_janela_roupas)
    valor_de_compra = Entry(cria_janela_roupas)
    valor_para_venda = Entry(cria_janela_roupas)
    data_de_compra = Entry(cria_janela_roupas)
    cor = Entry(cria_janela_roupas)

    cria_janela_roupas.mainloop()


# Executa a janela para visualização de dados gado
def janela_gados():
    cria_janela_gado = Tk()
    cria_janela_gado.title("Controle de gado")

    numero = Entry(cria_janela_gado)
    raca = Entry(cria_janela_gado)
    tipo = Entry(cria_janela_gado)
    peso = Entry(cria_janela_gado)
    m_ou_f = Entry(cria_janela_gado)
    prenha_ou_nao = Entry(cria_janela_gado)
    parida_ou_nao = Entry(cria_janela_gado)
    qual_pasto = Entry(cria_janela_gado)
    numero_mae = Entry(cria_janela_gado)
    numero_filho = Entry(cria_janela_gado)

    cria_janela_gado.mainloop()


# Executa janela inicial
janela_inicial = Tk()
janela_inicial.title("Controle de dados")
janela_inicial.geometry("400x400")

botão_Defensivos = Button(janela_inicial, text="Defensivos", command=janela_defensivos)
botão_Defensivos.grid(padx=150, pady=50)

botão_Roupas = Button(janela_inicial, text="Roupas", command=janela_roupas)
botão_Roupas.grid(padx=150, pady=51)

botão_Gado = Button(janela_inicial, text="Gado", command=janela_gados)
botão_Gado.grid(padx=150, pady=52)

janela_inicial.mainloop()



