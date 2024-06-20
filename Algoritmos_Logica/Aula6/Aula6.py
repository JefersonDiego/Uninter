# Tupla

# É uma estrutura de dados estática.
# A tupla é imutável.
# Representada no Python por parênteses ().
# Ex. Se for atribuída a uma tupla determidados dados,
# essa Tupla somente podrá trabalhar com essas dados.
# Não será possível atribuir novos dados a ela.

# mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
# print(mochila)

# # mochila[1] = 'Jaqueta'
# # print(mochila)

# for item in mochila:
#     print('A mochila possui: {}.'.format(item))

# tam = len(mochila)
# for i in range(0, tam, 1):
#     print('A mochila possui: {}.'.format(mochila[i]))

# upgrade = ('Queijo', 'Canivete')
# mochila_grande = mochila + upgrade

# print(mochila)
# print(upgrade)
# print(mochila_grande)

# Desempacotamento de parâmetros em funções

# def soma(*num):
#     acumulador = 0
#     print('Tupla: {}'.format(num))
#     for i in num:
#         acumulador += i
#     return acumulador

# print('Resultado: {}\n'.format(soma(1, 2)))
# print('Resultado: {}\n'.format(soma(1, 2, 3, 4, 5, 6, 7)))


# Listas

# Estrutura de dadods dinâmica
# Podemos alterar dados e tamanho
# Indexadas por valor numéricos inteiros
# Representada no Python pelos conchetes []

# mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
# print('Tupla: ', mochila)

# mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
# print('Lista: ', mochila)

# mochila[2] = 'Laranja'
# print('Lista: ', mochila)

# # Manipulando listas

# mochila.append('Ovos') # Adiciona na final da lista
# print('Lista: ', mochila)

# mochila.insert(1, 'Canivete') # insere na posição informada
# print('Lista: ', mochila)

# del mochila[1] # deleta o índice informado
# print('Lista: ', mochila)

# mochila.remove('Ovos') # delete o dado informado
# print('Lista: ', mochila)

# Referência de listas

# lista_original = [5, 7, 9, 11]
# lista_referenciada = lista_original

# print('Lista origial: {}'.format(lista_original))
# print('Lista referenciada: {}'.format(lista_referenciada))

# lista_original[0] = 2
# print('Lista origial: {}'.format(lista_original))
# print('Lista referenciada: {}'.format(lista_referenciada))
# # não é uma cópia, apenas faz uma referência a lista original
# # é como se tivesse outro nome, mas está olhando para o mesmo lugar

# # Cópia

# lista_original = [5, 7, 9, 11]
# lista_referenciada = lista_original[:]

# print('Lista origial: {}'.format(lista_original))
# print('Lista referenciada: {}'.format(lista_referenciada))

# lista_original[0] = 2
# print('Lista origial: {}'.format(lista_original))
# print('Lista referenciada: {}'.format(lista_referenciada))
# # agora fz de fato uma cópia

# # Strings e listas dentro de lista

# # Strings dentro de lista 
# mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
# print(mochila[0])

# mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
# print(mochila[0][0])
# print(mochila[2][1])

# print()

# mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
# for item in mochila:
#     for letra in item:
#         print(letra, end=' ')
#     print()

# print()

# mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
# for i in range(0, len(mochila), 1):
#     for j in range(0, len(mochila[i]), 1):
#         print(mochila[i][j], end=' ')
#     print()

# Listas dentro de listas

# Imagine uma situação na qual você deve realizar o cadastro de
# uma lista de compras em um sistema. Cada produto comprado deverá
# ser registrado com seu nome, quantidade e valor unitário.

# item = []
# mercado = []

# for i in range(3):
#     item.append(input('Digite o nome do item: '))
#     item.append(int(input('Digite a quantidade: ')))
#     item.append(float(input('Digite o valor: ')))
#     mercado.append(item[:])
#     item.clear()
# print(mercado)

# print()

# mercado = []

# for i in range(3):
#     nome = input('Digite o nome do item: ')
#     qtd = int(input('Digite a quantidade: '))
#     valor = float(input('Digite o valor: '))
#     mercado.append([nome, qtd, valor])
# print(mercado)

# soma = 0
# print('Lista de compras: ')
# print('-' * 20)
# print('item | quantidade | valor unitário | total do item')
# for item in mercado:
#     print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
#     soma += item[1] * item[2]
# print('-' * 20)
# print('Total a ser pago: {}'.format(soma))

# Dicionários

# Estrutura de dados dinâmica
# Podemos alterar dados e tamanho
# Indexados por chaves (palavras-chave)
# Representado em Python por chaves {}

# mochila = ('Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos')
# print('Tupla: ', mochila)

# print()

# mochila = ['Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos']
# print('Lista: ', mochila)

# print()

# mochila = {'Laptop':1, 'Smartphone':2, 'Power Bank':3, 'Carregadores e Cabos':4}
# print('Dicionário: ', mochila)

# print()

# game = {'nome':'Super Mario',
#         'desenvolvedora':'Nintendo',
#         'ano':1990}
# print(game)

# print()

# print(game['nome'])
# print(game['desenvolvedora'])
# print(game['ano'])

# # Métodos para dicionários

# print(game.values())
# print(game.keys())
# print(game.items())

# print()

# for keys in game.keys():
#     print(keys)
    
# print()

# for keys, values in game.items():
#     print('{} = {}'.format(keys, values))


# Listas com dicionários

games = []
game1 = {'nome':'Super Mario',
         'videogame':'Super Nintendo',
         'ano':1990}
game2 = {'nome':'Zelda Ocarina of Time',
         'videogame':'Nintendo 64',
         'ano':1998}
game3 = {'nome':'Pokemon Yellow',
         'videogame':'Game Boy',
         'ano':1999}

games = [game1, game2, game3]
print(games)

game = {}
games = []

for i in range(3):
    game['nome'] = input('Qual o nome do jogo? ')
    game['videogame'] = input('Para qual video-game ele foi lançado? ')
    game['ano'] = input('Qual o ano de lançamento? ')
    games.append(game.copy())
print('-' * 20)
print(games)
for jogos in games:
    for chave, valor in jogos.items():
        print('O campo {} tem o valor {}.'.format(chave, valor))

# Dicionários com listas

# games = {'nome':['Super Mario', 'Zelda Ocarina of Time', 'Pokemon Yellow'],
#          'videogame':['Super Nintendo', 'Nintendo 64', 'Game Boy'],
#          'ano':[1990, 1998, 1999]}
# print(games)

# games = {'nome':[], 'videogame':[], 'ano':[]}
# for i in range(3):
#     nome = input('Qual o nome do jogo? ')
#     videogame = input('Para qual video-game ele foi lançado? ')
#     ano = input('Qual o ano de lançamento? ')
#     games['nome'].append(nome)
#     games['videogame'].append(videogame)
#     games['ano'].append(ano)
# print('-' * 20)
# print(games)


# Trabalhando com métodos em strings

# Uma string assim com a a tupla, é imutável.
# Porém é possivel fazer uma alteração na string, utilizando uma lista,
# para torná-la mutável.

# s1 = 'Algoritmos'
# print(s1)
# s1[0] = 'a' # Não é possível fazer isso
# print(s1)


# s1 = list('Algoritmos')
# print(s1) # print separado
# print(''.join(s1)) # print agrupado

# Verificando caracteres

# s1 = 'Lógica de Programação e Algoritmos'
# print(s1.startswith('Lógica'))
# print(s1.endswith('algoritmos'))
# print(s1.lower().endswith('algoritmos'))
# print(s1.upper())
# print(s1.lower())

# print()

# print(s1.count('a'))

# print(s1.lower().count('a'))

# s1 = 'Um mafagafinho, dois mafagafinhos, três mafagafinhos ...'
# print(s1.lower().count('mafagafinhos'))

# print(s1.split(' '))

# print(s1.replace('mafagafinho', 'gatinho'))

# print(s1.replace('mafagafinho', 'gatinho', 1))

# # Validando tipo de dados

# s1 = 'Lógica de Programação e Algoritmos'
# s2 = '42'

# print(s1.isalnum()) # False, pois tem espaço junto (aceita somente letras e números)
# print(s2.isalnum()) # Somente números

# print(s1.isalpha()) # False, somente letras e acentos
# print(s2.isalpha())

# s1 = 'LógicadeProgramaçãoeAlgoritmos'
# print(s1.isalpha()) # True, possui somente letras