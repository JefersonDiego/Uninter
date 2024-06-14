# Funções

'''

print('|','--' * 10,'|')
print('|','--' * 10,'|')
print('          MENU')
print('|','--' * 10,'|')
print('|','--' * 10,'|')

print('')

def realce():
    print('|','--' * 10,'|')
    print('|','--' * 10,'|')

realce()
print('          MENU')
realce()

print('')

def realce(s1):
    print('|','--' * 10,'|')
    print('|','--' * 10,'|')
    print(s1)
    print('|','--' * 10,'|')
    print('|','--' * 10,'|')
    
realce('          MENU')

print('')

def soma(x, y):
    res = x + y
    print(res)
    
soma(13, 21)
soma(y = 20, x = 20)

print('')

def sub2(x = 1, y = 1):
    res = x - y
    print(res)

sub2()
'''

# Exercício

# Escreva uma rotina que vrie uma borda ao redor de uma palavra, para destacá-la
# como sendo um título. A rotina deve receber como parâmetro a palavra a ser
# destacada. O tamanho da caixa de texto deverá ser adaptável, de acordo com o
# tamanho da palavra.

'''
palavra = input('Digite uma palavara: ')

def destaque(palavra):
    tamanho = len(palavra)
    if tamanho:
        print('+', '-' * tamanho, '+')
        print('|', palavra, '|')
        print('+', '-' * tamanho, '+')

destaque(palavra)
'''

# Escopo de variáveis

'''
def omelete():
    ovos = 12

omelete()
# print(ovos)
# # a variável ovos não possui escopo global,
# ela só existe dentro da função omelete
'''

'''
def omelete():
    ovos = 12
    bacon()
    print(ovos)

def bacon():
    ovos = 6
# apesar da veriável ovos receber 6, ela não altera o conteúdo da variável
# dentro de omelete, pois ambas estão no escopo local de cada função

omelete()
'''

'''
def omelete():
    ovos = 12
    print('Ovos (omelete)= ', ovos)

def bacon():
    ovos = 6
    print('Ovos (bacon) = ', ovos)
    omelete()
    print('Ovos (bacon) = ', ovos)

ovos = 2
bacon()
print('Ovos (principal)= ', ovos)
'''

# Instrução global
# Força o algoritmo a não criar uma variável local de mesmo nome e
# manipular somente a global dentro de uma função

'''
def omelete():
    global ovos
    ovos = 6

ovos = 12
omelete()
print(ovos)
'''

'''
def omelete():
    global ovos
    ovos = 6
    bacon()

def bacon():
    ovos = 12
    pimenta()

def pimenta():
    print(ovos)
    

ovos = 4
omelete()
print(ovos)
'''


# Retorno de valores

'''
def soma3(x = 0, y = 0, z = 0):
    res = x + y + z
    return res

retornado = soma3(1, 2, 3)
print(retornado)

retornado1 = soma3(1, 2, 3)
retornado2 = soma3(1, 2)
retornado3 = soma3(1)

print(retornado1, retornado2, retornado3)
'''

# Exercício
# Escreva uma função para validar uma string. Essa função recebe
# como parâmetro a string, o número mínimo e máximo de caracteres.
# Retorne verdadeiro se o tamanho da string estiver entre os valores
# de mínimo e máximo, e falso, caso contrário.

'''
def valida_string(pal, min, max):
    if (len(pal) >= min and len(pal) <= max):
        return True
    else:
        return False

palavra = input('Digite uma palavra: ')
minimo = int(input('Digite um valor para o mínimo de caracteres: '))
maximo = int(input('Digite um valor para o máximo de caracteres: '))

tamanho_string = valida_string(palavra, minimo, maximo)

if (tamanho_string):
    print('O tamanho da string está correto.')
else:
    print('O tamanho da string está incorreto.')
'''
'''
def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1

x = valida_string('Digite uma string: ', 10, 30)
print('Você digitou a string: {}.\nDado válido. Encerrando o programa...'.format(x))
'''

# Tratamento de erros
'''
while True:
    try:
        x = int(input('Por favor digite um número: '))
        break
    except ValueError:
        print('Número inválido. Tente novamente...')
'''

'''
i = 0
while True:
    try:
        nome = input('Por favor digite o seu nome: ')
        ind = int(input('Digite o índice do seu nome digitado: '))
        print(nome[ind])
        break
    except ValueError:
        print('Nome inválido. Tente novamente.')
    except IndexError:
        print('Índice inválido. tente novamente.')
    finally:
        print('Tentativa {}.'.format(i))
        i += 1
'''

'''
def div():
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Erro de divisão por zero.')
    except:
        print('Algo deu errado.')
    else:
        return res
    finally:
        print('Executará sempre.')

print(div())
'''

#Funções lambda
# Funções simples, sem nome
# Podem ser escritas em uma só linha dentro do código

'''
res = lambda x: x * x
print(res(3))

soma = lambda x, y: x + y
print(soma(3, 5))
'''

# Faça uma função lambda que receba dois valores numéricos como parâmetro.
# Ao primeiro valor, sempre some 5. Em seguida, multiplique ambos e retorne
# o resultado

res = lambda x, y: (x + 5) * y
print(res(1, 10))