# Exercícios

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
'''

# Expressões lógicas/booleanas

'''
x = 10
y = 1

res = not x > y
print(res)

x = 10
y = 1
z = 5.5

res = (x > y) and (z == y)
print(res)


x = 10
y = 1
z = 5.5

res = x > y or not z == y and y != y + z / x
print(res)
'''

# Exercícios parte 2

# Um aluno, para passar de ano, precisa ser aprovado em todas as matérias
# que está cursando.
# Assuma que a média para aprovação é a partir de 7 e que o aluno cursa 3
# matérias, somente. Escreva um algoritmo que leia a nota final do aluno em
# cada matéria e informe, na tela, se ele passou de ano ou não.

nota1 = float(input("Digita a nota da primeira matéria: "))
nota2 = float(input("Digita a nota da segunda matéria: "))
nota3 = float(input("Digita a nota da terceira matéria: "))

# if ( (nota1 + nota2 + nota3) >= 21 ):

if ( (nota1 >= 7) and (nota2 >=7) and (nota3) >=7 ):
    print('Passou de ano.')
else:
    print('Não passou de ano.')