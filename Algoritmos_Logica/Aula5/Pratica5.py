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

# Função que valida a opção do menu
def valida_opcao(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

# Função que verifica a existência do arquivo
def arquivoExiste(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# Função que cria um arquivo
def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print('Arquivo \"{}\" criado com sucesso.\n'.format(arquivo))

# Função que cadastra um jogo
def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir arquivo.')
    else:
        a.write('{};{}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()

# Função que lista o arquivo
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        print(a.read())
    finally:
        a.close()
        

# Criação do arquivo

arquivo = 'games.txt'
if arquivoExiste(arquivo):
    print('O arquivo já foi criado.')
else:
    print('Arquivo não encontrado.')
    criarArquivo(arquivo)



while True:
    print('+------------------+')
    print('|-------MENU-------|')
    print('|------------------|')
    print('|1. NOVO ITEM------|')
    print('|2. LISTAR TUDO----|')
    print('|3. SAIR-----------|')
    print('+------------------+')
    opcao = valida_opcao('Digite uma opção: ', 1, 3)

    if (opcao == 1):
        print('Opção Novo item')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif (opcao == 2):
        print('Opção listar tudo')
        listarArquivo(arquivo)
    elif (opcao == 3):
        print('Saindo...')
        break



