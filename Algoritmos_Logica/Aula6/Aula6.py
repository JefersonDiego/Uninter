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

lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original

print('Lista origial: {}'.format(lista_original))
print('Lista referenciada: {}'.format(lista_referenciada))

lista_original[0] = 2
print('Lista origial: {}'.format(lista_original))
print('Lista referenciada: {}'.format(lista_referenciada))
# não é uma cópia, apenas faz uma referência a lista original
# é como se tivesse outro nome, mas está olhando para o mesmo lugar

# Cópia

lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original[:]

print('Lista origial: {}'.format(lista_original))
print('Lista referenciada: {}'.format(lista_referenciada))

lista_original[0] = 2
print('Lista origial: {}'.format(lista_original))
print('Lista referenciada: {}'.format(lista_referenciada))
# agora fz de fato uma cópia

