# Exercício

#Condicional simples

# Desenvolva um programa que leia dois valores numéricos inteiros e compare se
# o primeiro é maior do que o segundo, utilizando uma condicional simples.
# Caso seja (resutado verdadeiro), ele imprime na tela a mensagem informando
# que o primeiro valor digitado é maior do que o segundo.

'''
val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))

if (val1 > val2):
    print('O primeiro valor é maior do que o segundo.')
'''

# Lê dois valores inteiro e compara ambos

'''
val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))

if (val1 > val2):
    print('O primeiro valor é maior do que o segundo.')
    
if (val2 > val1):
    print('O segundo valor é maior do que o primeiro.')
'''

# Condicional composta

'''
val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor diferente do primeiro: '))

if (val1 > val2):
    print('O primeiro valor é maior do que o segundo.')
else:
    print('O segundo valor é maior do que o primeiro.')
'''

'''
val = int(input('Digite um número: '))

if ((val % 2) == 0):
    print('Número par.')
else:
    print('Número ímpar.')
'''

# not
x = True
y = False

print(not x)
print(not y)

# and
print(x and y)
print(x and x)

# or
print(x or y)
print(x or x)
print(y or y)