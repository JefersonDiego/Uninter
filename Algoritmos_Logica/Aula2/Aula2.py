# Ciclo de processamento de dados
# <------------------------------------->


#Comando de saída
print('Hello, word')
print("Hello, word")

#Operação aritmética
print(2 + 3)

#Imprime uma string
print('2 + 3')

#Concatenação
print('2' + '3')

#Concatenando mensagens
print('Hello,' + ' world')
print('Hello,','world')

#Concatenando mensagens e números
print('O resultado da soma de 2 + 3 é:', 2 + 3)

#Ordem de precedência em cáclulos
print(10 * (5 + 7) / 4)

#Diferente de
print(10*(5 + 7 / 4))


# Variáveis, dados e seus tipos
# <------------------------------------->

nota = 8.5
disciplina = 'Lógica de Programação e Algoritmos'

print(nota)
print(disciplina)

print('Disciplina: ', disciplina, '. Nota: ', nota)

a = 1 #a recebe 1
b = 5 #b recebe 5

resposta = a == b
print(resposta)

resposta = a != b
print(resposta)

idade = input('Qual sua idade? ')
print(idade)

nome = input('Qual o seu nome? ')
print(f'Olá {nome}, seja bem-vindo!')

nota = float(input('Qual nota você recebeu na disciplina? '))
print(f'Você tirou nota {nota}.')


x = 1 # x = 1
y = 1 # y = 1
z = x + y # z = 2 (1 + 1)

x = x + 2 # x = 3 (1 + 2)
y = y - 1 # y = 0 (1 - 1)
z = x + y # z = 3 (3 + 0)

x = y + 1 # x = 1 (0 + 1)
y = x - 1 # y = 0 (1 - 1)
z = x + y # z = 1

print(z)

#Desenvolva um algoritmo que solicite ao usuários dois números inteiros.
#Imprima a soma desses dois números na tela.

print('-Soma de dois números-')
num1 = int(input('Digite o primeiro número inteiro:'))
num2 = int(input('Digite o segundo número inteiro:'))

print('A soma de {} com {} é {}.'.format(num1, num2, num1+num2))