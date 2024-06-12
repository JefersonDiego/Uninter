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
'''
nota1 = float(input("Digita a nota da primeira matéria: "))
nota2 = float(input("Digita a nota da segunda matéria: "))
nota3 = float(input("Digita a nota da terceira matéria: "))

# if ( (nota1 + nota2 + nota3) >= 21 ):

if ( (nota1 >= 7) and (nota2 >=7) and (nota3) >=7 ):
    print('Passou de ano.')
else:
    print('Não passou de ano.')
'''

# Condicionais aninhadas

# Escreva um algoritmo em Python em que o usuário escolhe se quer comprar maçãs,
# laranjas ou bananas. Deverá ser apresentado na tela um menu com as opções:
# 1 para maçã, 2 para laranja e 3 para banana.
# Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O
# algoritmo deve calcular o preço total a pagar pelo produto escolhido e mostrá-lo
# na tela.
# Considere que uma maçã custa R$2,30, uma laranja, R$3,60 e uma banana, 1,85

maca = 2.3
laranja = 3.6
banana = 1.85
quantidade = 0
opcao = int(input('Digite a opção que deseja comprar conforme menu abaixo:\n1. Maçã (R$2,30)\n2. Laranja(R$3,60\n3. Banana(R$1,85)\n'))
quantidade = int(input('Quantas unidades deseja comprar? '))

if (opcao == 1):
    preco_total = quantidade * maca
    produto_existe = 1
else:
    if (opcao == 2):
        preco_total = quantidade * laranja
        produto_existe = 1
    else:
        if (opcao == 3):
            preco_total = quantidade * banana
            produto_existe = 1
        else:
            produto_existe = 0

if (produto_existe == 1):
    print('Valor total a pagar R${0:.3g}.'.format(preco_total))
elif (produto_existe != 1):
    print('Produto não existe.')