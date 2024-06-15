# Docstring

# Texto inserido na função que explica o funcionamento dela
# Texto entre ''' ''' é uma docstring e não um comentário

# def soma3(x =0, y = 0, z = 0):
    
#     '''
    
#     Função que retorna a soma 2 ou 3 números.
#     Caso não seja passado o valor de um dos parâmetros,
#     este recebe 0.
    
    
#     '''
    
#     return x + y + z

# print(soma3(3, 3, 3))
# help(soma3)


# Prática

# Exercício 1

# Escreva uma função que calcule o fatorial de um número recebido
# como parâmetro e retorne o seu resultado.
# Faça uma validação dos dados por meio de uma outra função,
# permitindo que somente valores positivos sejam aceitos.
# Crie o help da sua função.

# def fatorial(num):
    
#     '''
#     Função fatorial:
#     Recebe um número inteiro maior ou igual a 0 e calcula o seu fatorial.
#     Ex: 4! = 4 x 3 x 2 x 1 
#     '''
    
#     fat = 1
#     if (num == 0):
#         return fat
#     if (positivo(num)):
#         for i in range(num, 0, -1):
#             fat *= i
#         return fat
#     if (not(positivo(num))):
#         return False


# positivo = lambda num: num > 0

# num = int(input(' Digite um número, positivo, para o cálculo da fatorial: '))
# if (fatorial(num)):
#     print('{}! = {}'.format(num, fatorial(num)))
# if (not(fatorial(num))):
#     print('Você digitou um número negativo.')

# Exercício 3

# Suponha que você é um colecionador de jogos de videogames. Escreva um algoritmo
# que permita cadastrar esses jogos informando o nome e a qual videogame ele pertence.
# Para isso, crie um menu de opções contendo:
# Cadastrar novo item, listar tudo o que foi cadastrado e sair
# Para resolver esse exercício, crie pelo menos uma função para cada item do menu.
# Além disso, armazene todos os dados em um arquivo de texto que deve ser salvo em
# disco e manter os dados cadastrados.

print('+------------------+')
print('|-------MENU-------|')
print('|------------------|')
print('|1. NOVO ITEM------|')
print('|2. LISTAR TUDO----|')
print('|3. SAIR-----------|')
print('+------------------+')
opcao = int(input('Digite uma opção: '))


