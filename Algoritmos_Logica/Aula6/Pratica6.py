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

from statistics import mean

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# Encontrar quantos alunos tiraram nota 7
nota = 7
print('{} alunos tiraram nota {}'.format(notas.count(nota), nota))

# Alterar a última nota para 4
notas[-1] = 4
print(notas)

# Encontrar a maior nota
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print('Maior nota: {}'.format(max(notas)))
print('Notas ordenadas: {}'.format(sorted(notas)))
print('Média das notas: {}'.format(mean(notas)))