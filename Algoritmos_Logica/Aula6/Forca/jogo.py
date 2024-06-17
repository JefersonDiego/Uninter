import desenhos as d
import fileHandler as fh
from random import choice

def jogar():
    lista_palavras = []
    arquivo = fh.abrirArquivoLeitura('palavras.txt')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)

palavra_sorteada = choice(lista_palavras)

for x in range(50):
    print() #50 linhas em branco para sumir com o menu

digitadas = []
acertos = []
erros = []

nome = input('Quem está jogando? ')

while True:
    adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)
    # CONDIÇÃO DE VIRÓRIA