# Estrutura de repetição While (enquanto)
'''
x = 1

while (x <= 5):
    print(x)
    x += 1

# Contadores

inicial = int(input('Valor inicial: '))
final = int(input('Valor final: '))

x = inicial
while ( x <= final):
    #Verifica se é par
    if (x % 2 == 0):
        print(x)
    x += 1


# Acumuladores

soma = 0
cont = 1

while (cont <= 5):
    x = float(input('Digite a {}ª nota: '.format(cont)))
    soma = soma + x
    cont += 1
media = soma / 5
print('Média final: {}'.format(media))
'''

# Exemplo
# Crie um algoritmo que receba um valor do tipo inteiro via teclado.
# No entanto, o programa só deve aceitar, obrigatoriamente, valores
# inteiro e positivos.
# Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo
# programa e um novo valor solicitado.

'''
valor = int(input('Digite um valor inteiro e positivo: '))

while (valor <= 0 ):
    valor = int(input('Valor inválido. Digite um valor inteiro e positivo: '))

if (valor > 0):
    print('Valor correto.')
'''

# Exercício

# Escreva um algoritmo que fique recebendo frases ou palavras digitadas
# pelo usuário.
# Encerre o algoritmo quando a palavra "sair" for digitada.

'''
while True:
    palavras = input('Digite algumas palavras: ')
    if (palavras == 'sair'):
        print('Encerrando...')
        break
'''

# Escreva um algoritmo em que o usuário realize um login em um sistema.
# O usuário deve informar seu nome e senha

'''
nome = 'Pedro'
senha = 'pedropedropedro'

while True:
    nome_digitado = input('Digite o nome de usuário: ')
    senha_digitada = input('Digite a senha: ')
    if ((nome_digitado == nome) and (senha_digitada == senha)):
        break
    print('Nome ou senha inválida. Tente novamente...')

print('Login efetuado com sucesso.')
'''

# Valores Truthy e Falsey
# O Python interpreta o valor 1 como True e valor 0 como False
# Também interpreta uma string vazia (sem caracteres ou espaço)
# como False e uma string com conteúdo como True

'''
nome = ''

while not nome:
    # String vazia é false, o not torna true, quando a string estiver
    # com conteúdo, o not torna ela false e o laço acaba
    nome = input('Digite seu nome: ')
'''

# Estrutura de repetição For (para)

'''
for i in range(5):
    print(i)
    
print('')

for i in range(1,5,1):
    print(i)
'''

'''
frase = 'Lógica de Programação e Algoritmos'
for i in range(0, len(frase), 1):
    print(frase[i], end='')
'''

# Escreva um algoritmo que calcule a média dos números pares de 1 a 100
# (1 e 100 inclusos). Implemente o laço for.

x = 0
cont = 0
for i in range(1,101,1):
    if (i % 2 == 0):
        x += i
        cont += 1

print('A média é {}'.format(x/cont))