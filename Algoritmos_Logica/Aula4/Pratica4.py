# While x For
# Realize a sequência de print com for e while:

# Inteiros de 3 até 12, com 12 incluso

'''
# While
i = 3
while (i <= 12):
    print(i)
    i += 1

print('')

# For

for i in range(3,13):
    print(i)

print('*******************************')

# Inteiros de 0 até 9, excluindo 9, com passo 2

# While
i = 0
while (i < 9):
    print(i);
    i += 2

print('')

# For
for i in range(0,9,2):
    print(i)
'''

# Exercício 1

#Escreva um algoritmo que mostra, na tela, quatro produtos a serem comprados
# em uma lanchonete:
# Coxinha - R$ 5,00
# Pastel - R$ 7,00
# Café - R$ 4,00
# Suco - R$ 6,00

# Faça um algoritmo em que você seleciona o produto que quer comprar
# e a quantidade. Faça isso até que decida encerrar o programa.
# Ao final, mostre o valor final do pedido a ser pago.

'''

print('Cardápio:\n1 - Coxinha - R$ 5,00\n2 - Pastel  - R$ 7,00\n3 - Café    - R$ 4,00\n4 - Suco    - R$ 6,00\n5 - SAIR')


total = 0
quantidade = 0

coxinha = 5
pastel = 7
cafe = 4
suco = 6

while True:
    opcao = int(input('Esolha um produto ou SAIR: '))
    if (opcao == 5):
        print('Saindo...')
        break;
    elif (opcao == 1):
        quantidade = int(input('Quantas unidade quer comprar? '))
        total = total + coxinha * quantidade
    elif (opcao == 2):
        quantidade = int(input('Quantas unidade quer comprar? '))
        total = total + pastel * quantidade
    elif (opcao == 3):
        quantidade = int(input('Quantas unidade quer comprar? '))
        total = total + cafe * quantidade
    elif (opcao == 4):
        quantidade = int(input('Quantas unidade quer comprar? '))
        total = total + suco * quantidade
    else:
        opcao = int(input('Opção inválida. Selecione outro produto ou SAIR: '))
        

print('O valor total do seu pedido foi de R${}.'.format(total))
'''

# Exercício 2

# Escreva um algoritmo que leia um valor e que imprima a quantidade de
# cédulas necessárias para pegar esse mesmo valor. para simplificar,
# vamos trabalhar apenas com valores inteiros e com cédula de R$100,
# R$50, R$20, R$10, R$5 e R$1

'''
valor = int(input('Digite o valor que você deseja: '))

notas_100 = valor // 100
valor = valor % 100

notas_50 = valor // 50
valor = valor % 50

notas_20 = valor // 20
valor = valor % 20

notas_10 = valor // 10
valor = valor % 10

notas_5 = valor // 5
valor = valor % 5

notas_1 = valor // 1
valor = valor % 1

print('Notas de 100: {}'.format(notas_100))
print('Notas de 50: {}'.format(notas_50))
print('Notas de 20: {}'.format(notas_20))
print('Notas de 10: {}'.format(notas_10))
print('Notas de 5: {}'.format(notas_5))
print('Notas de 1: {}'.format(notas_1))
'''

'''
# Usando laço
valor = int(input('Digite o valor que você deseja: '))
while valor:
    if valor >= 100:
        notas_100 = valor // 100
        valor = valor  - notas_100 * 100
        print('Notas de 100: {}'.format(notas_100))
    
    if valor >= 50:
        notas_50 = valor // 50
        valor = valor  - notas_50 * 50
        print('Notas de 50: {}'.format(notas_50))

    if valor >= 20:
        notas_20 = valor // 20
        valor = valor  - notas_20 * 20
        print('Notas de 20: {}'.format(notas_20))

    if valor >= 10:
        notas_10 = valor // 10
        valor = valor  - notas_10 * 10
        print('Notas de 10: {}'.format(notas_10))

    if valor >= 5:
        notas_5 = valor // 5
        valor = valor  - notas_5 * 5
        print('Notas de 5: {}'.format(notas_5))

    if valor:
        notas_1 = valor
        valor = valor  - notas_1
        print('Notas de 1: {}'.format(notas_1))
'''

# Exercicio 3

# Um cinema cobra preços diferentes para os ingressos, de acordo com a idade
# da pessoa. Se a pessoa tiver menos de 3 anos de idade, o ingresso será gratuito;
# se tiver entre 3 e 12 anos, o ingresso custará R$15; se tiver mais de 12 anos,
# custará R$30.
# Escreva um laço em que você pergunta a idade aos usuários e, então, informe-lhes
# o preço do ingresso do cinema.
# Encerre o laço udando um break quando o usuário digitar 0.
# Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos,
# o total de dinheiro arrecadado e a média de idade das pessoas.

idade = int(input('TABELA DE PREÇO\nMenores de 3 anos: Gratuito\nEntre 3 e 12 anos: R$15,00\nMaiores de 12 anos: R$30,00\nPara SAIR digite 0.\n'))
clientes = 0
bilheteria = 0
soma_idades = 0

while idade > 0:
    if (idade <= 0):
        break;    
    elif (idade > 0 and idade < 3):
        clientes += 1
        soma_idades += idade
    elif (idade >= 3 and idade <= 12):
        bilheteria += 15
        clientes += 1
        soma_idades += idade
    elif (idade > 12):
        bilheteria += 30
        clientes += 1
        soma_idades += idade
    idade = int(input('Próximo cliente: '))

if (clientes != 0):
    print('Total de clientes: {}\nBilheteria: R${}\nMédia de idade: {} anos\n'.format(clientes, bilheteria, soma_idades/clientes))
else:
    print('Saindo...')