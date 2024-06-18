def validaSabor(pergunta):
    while True:
        try:
            sabor = input(pergunta).lower()
            if (sabor == 'ba') or (sabor == 'ff'):
                return sabor
            else:
                print('Sabor inválido. Tente novamente.\n')
        except:
            print('Valor não reconhecido.\n')
        # caso seja informado algum caractere diferente volta para
        # o início do laço

def validaTamanho(pergunta):
    while True:
        try:
            tamanho = input(pergunta).lower()
            # transforma a entrada em minúscula, assim, aceita
            # tanto caracteres maiúsculos quanto minúsculos
            if (tamanho == 'p') or (tamanho == 'm') or (tamanho == 'g'):
                return tamanho
            else:
                print('Tamanho inválido. Tente novamente.\n')
        except:
            print('Valor não reconhecido.\n')

def validaPergunta(pergunta):
    while True:
        try:
            continuar = input(pergunta).lower()
            if (continuar == 's') or (continuar == 'n'):
                return continuar
            else:
                print('Resposta inválida. Tente novamente.')
        except:
            print('Valor não reconhecido.')

valor = 0

print('------Bem-vindo a tele-entrega do Jéferson Diego Leidemer-----')
print('---------------------------CARDÁPIO---------------------------')
print('-' * 62)
print('----| Tamanho | Bife Acebolado (BA) | Filé de Frango(FF) |----')
print('----|    P    |      R$16.00        |      R$ 15.00      |----')
print('----|    M    |      R$18.00        |      R$ 17.00      |----')
print('----|    G    |      R$22.00        |      R$ 21.00      |----')
print('-' * 62)

while True:
    sabor = validaSabor('Digite o sabor desejado (BA/FF): ')
    tamanho = validaTamanho('Digite o tamanho desejado (P/M/G): ')
    if (sabor == 'ba'):
        if (tamanho == 'p'):
         valor += 16
         print('Você pediu um Bife Acebolado no tamanho P: R$16.00')
        if (tamanho == 'm'):
            valor += 18
            print('Você pediu um Bife Acebolado no tamanho M: R$18.00')
        if (tamanho == 'g'):
            valor += 22
            print('Você pediu um Bife Acebolado no tamanho G: R$22.00')
    elif (sabor == 'ff'):
        if (tamanho == 'p'):
            valor += 15
            print('Você pediu um Filé de Frango no tamanho P: R$15.00')
        if (tamanho == 'm'):
            valor += 17
            print('Você pediu um Filé de Frango no tamanho M: R$17.00')
        if (tamanho == 'g'):
            valor += 21
            print('Você pediu um Filé de Frango no tamanho G: R$21.00')
    
    continuar = validaPergunta('\nDeseja mais alguma coisa: (S/N) ')
    if (continuar == 's'):
        continue # volta para o início do laço
    elif (continuar == 'n'):
        break # sai do laço
    
print('Valor total: R${0:.2f}'.format(valor))