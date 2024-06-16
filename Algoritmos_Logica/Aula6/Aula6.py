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