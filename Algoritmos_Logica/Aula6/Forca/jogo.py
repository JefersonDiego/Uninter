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
    erros = 0

    nome = input('Quem está jogando? ')

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)
        # CONDIÇÃO DE VITÓRIA
        if adivinha == palavra_sorteada:
            print('Você acertou!')
            break
        
        # TENTATIVA
        tentativa = input('\nDigite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('Você já usou esta letra.')
            continue
        else:
            digitadas.append(tentativa)
            if tentativa in palavra_sorteada:
                acertos.append(tentativa)
            else:
                erros += 1
                print('Você errou.')
                
        
        score = d.desenhar_forca(erros)
        
        # CONDIÇÃO DE FIM DE JOGO
        if erros == 6:
            print('Enforcado!!')
            print('A palavra correta era {}.'.format(palavra_sorteada))
            break
        
    fh.inserir_score('score.txt', nome, score)
    