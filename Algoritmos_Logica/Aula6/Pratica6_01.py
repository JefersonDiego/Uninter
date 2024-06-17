# import math
# import math as m
# cria um apelido para a biblioteca
# mais recomendado é importar somente os métodos necessários
# from math import sqrt

# print(math.sqrt(9))
# print(sqrt(9))
# importando somente a função não é necessário informar a biblioteca

# Exercícios Listas

# Dada uma lista contendo as notas de alunos em uma disciplina,
# escreva uma expressão para:
# notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# # Encontrar quantos alunos tiraram nota 7
# nota = 7
# print('{} alunos tiraram nota {}'.format(notas.count(nota), nota))

# # Alterar a última nota para 4
# notas[-1] = 4
# print(notas)

# # Encontrar a maior nota
# notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# print('Maior nota: {}'.format(max(notas)))
# print('Notas ordenadas: {}'.format(sorted(notas)))
# print('Média das notas: {}'.format(sum(notas) / len(notas)))

# Exercício 1

# Escreva um algoritmo que crie uma tupla com 10 palavras. Encontre dentro
# dessa tupla as vogais de cada palavra. Faça um print na tela com o nome
# da palavra e suas respectivas vogais.

# def eh_vogal(palavra):
#     vogais = []
#     palavra = palavra.lower()
#     for i in palavra:
#         if i in 'aeiou':
#             vogais.append(i.upper())
#     return vogais

# games = ('Mario', 'Zelda OoT', 'Metroid', 'Donkey Kong', 'Pokemon Yellow', 'Kirby', 'Animal Crossing', 'Luigi Mansion', 'Pikmin', 'Harvest Moon')

# for i in games:
#     print('{} : {}'.format(i.upper(), eh_vogal(i)))


# Exercício 2

# Crie um jogo de pedra, papel ou tesoura (Jokenpô).
# Você deverá jogar contra o computador. Você irá sempre
# escolher uma das opções: 1 - pedra, 2 - papel e 3 - tesoura.
# O computador irá sempre sortear um número de 1 a 3 para jogar.
# Armazene todos os resultados em uma lista e, no final, apresente
# o vencedor.
# Encerre o programa ao digitar zero.

# from random import randrange

# placar = []
# pontos_jogador = 0
# pontos_computador = 0
# pontos_empate = 0

# def valida_opcao(pergunta, min, max):
#     try:
#         x = int(input(pergunta))
#         while ((x < min) or (x > max) ):
#             x = int(input(pergunta))
#         return x
#     except ValueError:
#         print('Algo deu errado...')

# def jogada(jogador, computador):
#     if ((jogador == 1) and (computador == 3)):
#         return 'jogador'
#     if ((jogador == 2) and (computador == 1)):
#         return 'jogador'
#     if ((jogador == 3) and (computador == 2)):
#         return 'jogador'
#     if ((computador == 1) and (jogador == 3)):
#         return 'computador'
#     if ((computador == 2) and (jogador == 1)):
#         return 'computador'
#     if ((computador == 3) and (jogador == 2)):
#         return 'computador'
#     if (jogador == computador):
#         return 'empate'

# def exibe_placar(placar):
#     jogador = 0
#     computador = 0
#     empate = 0
#     resultado = []
#     for i in placar:
#         if i == 'jogador':
#             jogador += 1
#         if i == 'computador':
#             computador += 1
#         if i == 'empate':
#             empate += 1
    
#     resultado = [jogador, computador, empate]
#     return resultado

# def vencedor(p_jogador, p_computador):
#     if (p_jogador > p_computador):
#         return 'Você venceu!!!'
#     if (p_jogador < p_computador):
#         return 'Você perdeu!!!'
#     if (p_jogador == p_computador):
#         return 'Empate'
        
# while True:

#     print('+-------------+')
#     print('|---JOKENPÔ---|')
#     print('|-------------|')
#     print('|1. PEDRA-----|')
#     print('|2. PAPEL-----|')
#     print('|3. TESOURA---|')
#     print('|0. SAIR------|')
#     print('+-------------+')

#     opcao = valida_opcao('Escolha a jogada: ', 0, 3)
#     if (opcao == 0):
#         break
#     jogada_computador = randrange(1, 4)
#     placar.append(jogada(opcao, jogada_computador))
    
#     pontos_jogador = exibe_placar(placar)[0]
#     pontos_computador = exibe_placar(placar)[1]
#     pontos_empate = exibe_placar(placar)[2]
#     #print('Jogador: {} - Computador: {} - Empate: {}'.format(pontos_jogador, pontos_computador, pontos_empate))

# print(vencedor(pontos_jogador, pontos_computador))
# print('Jogador: {} - Computador: {} - Empate: {}'.format(pontos_jogador, pontos_computador, pontos_empate))

from datetime import datetime

data = datetime.now()
ano = data.year

nomes = []
nascimento = []
sexo = []

total_cadastros = lambda cad:len(cad['nome'])

def media_idade(cad, ano):
    soma_ano = 0
    for i in cad['nascimento']:
        soma_ano += (ano - i)
    return int(soma_ano / total_cadastros(cad))

def menos_trinta(cad, sex):
    lista_nomes = []
    for i in range(total_cadastros(cad)):
        if (cad['sexo'][i] in sex):
            lista_nomes.append(cad['nome'][i])
    return lista_nomes

def idade_acima_media(cad, sex):
    lista_nomes = []
    media = media_idade(cad, ano)
    idade = 0
    for i in range(total_cadastros(cad)):
        idade = cad['nascimento'][i]
        if ((cad['sexo'][i] in sex) and (idade > media)):
            lista_nomes.append(cad['nome'][i])
    return lista_nomes
    
            
        
        


cadastro = {'nome':['Nome1', 'Nome2', 'Nome3', 'Nome4', 'Nome5', 'Nome6'], 'nascimento':[1980, 1980, 1993, 1949, 2006, 2000], 'sexo':['m', 'f', 'o', 'm', 'f', 'o']}


# while True:
#     nomes.append(input('Digite seu nome: '))
#     nascimento.append(int(input('Digite o ano do seu nascimento :')))
#     sexo.append(input('Digite M para masculino, F para feminino e O para outro: '))

#     cadastro = {'nome':nomes, 'nascimento':nascimento, 'sexo':sexo}
    
#     encerrar = input('Prencher outro cadastro? (S / N)')
#     if (encerrar in 'Nn'):
#         break
        
print('O total de cadastros foi de {} pessoas.'.format(total_cadastros(cadastro)))
print('A média de idade das pessoas é de {} anos.'.format(media_idade(cadastro, ano)))
print('Mulheres com menos de 30 anos: {}.'.format(menos_trinta(cadastro, 'f')))
print('Os seguintes humens possuem uma idade acima da média: {}'.format(idade_acima_media(cadastro, 'm')))





