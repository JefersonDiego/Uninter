# Exercíco 3 - Jogo da Forca

# Criar um jogo da forca, contendo as opções:
# 1 . Jogar
# 2. Score
# 3. Sair
# Para jogar, o jogador deverá adivinhar a palavra que será
# carregada de uma lista de palavras dentro de um arquivo de
# texto.
# Ao jogar, o nome do jogador deve ser perguntado.
# Este nome será armazenado no final da jogada, junto com o score
# que o jogador fez.
# O nome e o score devem ser armazenados dentro de um aruivo.
# Na opção de SCORE, mantenha salva a lista de jogadores e seus
# respectivos scores.
# Mostrer os scores na tela quando selecionar essa opção.

import jogo as j
import fileHandler as fh

def mostrarMenu():
    print('=' * 30)
    print(' ' * 7 + 'JOGO DA FORCA')
    print('=' * 30)
    print('1 - JOGAR')
    print('2 - SCORE')
    print('3 - SAIR')
    print('=' * 30)

arquivo = 'score.txt'

if (fh.existeArquivo(arquivo)):
    print('Arquivo localizado no computador.')
else:
    print('Aquivo não existe.')
    fh.criarArquivo(arquivo)

while True:
    mostrarMenu()
    opcao = int(input('Escolha a opção (1 | 2 | 3): '))

    match(opcao):
        case 1:
            print('Iniciar jogo...')
            
        case 2:
            print('SCORE')
        case 3:
            print('Saindo do jogo...')
            break
        case _:
            print('Opção inválida, tente outra.')
        