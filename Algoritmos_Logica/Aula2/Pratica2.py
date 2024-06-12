# Exercícios de fixação
# Somatório dos 5 primeiros números inteiros e positivos
print('Somatório de 1 + 2 + 3 + 4 + 5 é {}.'.format(1 + 2 + 3 + 4 + 5))

# Média entre 23, 19 e 31
print('A média entre 23, 19 e 31 é {}.'. format( (23 + 19 + 31) / 3 ))

# Numero de vezes qu o 73 cabe em 403
print('Número de vezes qu o 73 cabe em 403 é {}.'.format(403 // 73))

# A sobra quando 403 é dividido por 73
print('A sobra quando 403 é dividido por 73 é {}.'.format(403 % 73))

# 2 elevado à 10ª potência
print('2 elevado à 10ª potência é {}.'.format(2 ** 10))

# O valor absoluto da diferença entre 54 e 57
print('o valor absoluto da diferença entre 54 e 57 é {}.'.format( abs(54 - 57)))

# O menor valor entre 34, 29 e 31
print('O menor valor entre 34, 29 e 31 é {}.'.format(min([34, 29, 31])))

# Atribuir o valor inteiro 3 à variável a
a = 3

# Atribuir o valor inteiro 4 à variável b
b = 4

# Atribuir à variável c o valor da experessão a * a + b * b
c = a * a + b * b
print('O valor da variável a é {}, da variável b é {} e da expressão a * a + b * b é {}'.format(a, b, c))

# Execute as seguintes atribuições
# s1 = 'ant'
# s2 = 'bat'
# s3 = 'cod'

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# Agora utilizando operadores + e *, crie as saídas a seguir:
# a) 'ant bat cod'
# b) 'ant ant ant ant ant ant ant ant ant ant'
# c) 'ant bat bat cod cod cod'
# d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
# e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'

print (s1, s2, s3)
print((s1 + ' ') * 10)
print(s1, (s2 + ' ') * 2 + (s3 + ' ') * 3)
print((s1 + ' ' + s2 + ' ') * 7)
print(((s2 * 2) + s3 + ' ') * 5)