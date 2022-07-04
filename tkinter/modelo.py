import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_c["text"] = texto


janela = Tk()

janela.title("Cotação atual")

janela.geometry("400x400")

texto_o = Label(janela, text='Clique no botão para ver a cotação')

texto_o.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_c = Label(janela, text="")
texto_c.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
