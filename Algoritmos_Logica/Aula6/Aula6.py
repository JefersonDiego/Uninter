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

def soma(*num):
    acumulador = 0
    print('Tupla: {}'.format(num))
    for i in num:
        acumulador += i
    return acumulador

print('Resultado: {}\n'.format(soma(1, 2)))
print('Resultado: {}\n'.format(soma(1, 2, 3, 4, 5, 6, 7)))
