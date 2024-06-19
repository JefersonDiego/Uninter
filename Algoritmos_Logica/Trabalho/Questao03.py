def valida_modelo(pergunta):
    while True: # sai do laço somente depois de receber um entrada válida # [EXIGÊNCIA DE CÓDIGO 7 de 7]
        try: # [EXIGÊNCIA DE CÓDIGO 6 de 7]
            modelo = input(pergunta).lower()
            if (modelo == 'mcs') or (modelo == 'mls') or (modelo == 'mce' or (modelo == 'mle')):
                return modelo
            else:
                print('Modelo inválido. Tente novamente.\n')
        except:
            print('Valor não reconhecido.\n')

def valida_qtd(pergunta):
    while True:
        try:
            qtd = int(input(pergunta))
            if (qtd > 0) and (qtd <= 20000):
                return qtd
            elif (qtd > 20000):
                print('Não aceitamos tantas camisetas de uma vez.')
                print('Entre com a quantidade de camisetas novamente (entre 1 e 20000).')
            else:
                print('Quantidade inválida. Tente novamente.\n')
        except:
            print('Valor não reconhecido.\n')

def valida_frete(pergunta):
    while True:
        try:
            tipoFrete = int(input(pergunta))
            if (tipoFrete >= 0) and (tipoFrete <= 2):
                return tipoFrete
            else:
                print('Opção inválida. Tente novamente.\n')
        except:
            print('Valor não reconhecido.\n')

# EXIGÊNCIA DE CÓDIGO 2 de 7]
def escolha_modelo():
    modelo = valida_modelo('\nEntre com o modelo desejado: ')
    # [EXIGÊNCIA DE CÓDIGO 7 de 7]
    # chama a função valida_modelo() para garantir somente entradas válidas 
    if (modelo == 'mcs'):
        return 1.8
    elif (modelo == 'mls'):
        return 2.1
    elif (modelo == 'mce'):
        return 2.0
    elif (modelo == 'mle'):
        return 3.2

# [EXIGÊNCIA DE CÓDIGO 3 de 7]
def num_camisetas():
    qtd = valida_qtd('\nDigite a quantidade de camisetas: ')
    if ((qtd >= 20) and (qtd < 200)):
        return (qtd - (qtd * 0.05))
    elif ((qtd >= 200) and (qtd < 2000)):
        return (qtd - (qtd * 0.07))
    elif ((qtd >= 2000) and (qtd < 20000)):
        return (qtd - (qtd * 0.12))
    else:
        return qtd

# [EXIGÊNCIA DE CÓDIGO 4 de 7];
def frete():
    tipoFrete = valida_frete('\nEscolha o tipo de frete: ')
    if (tipoFrete == 1):
        return 100
    elif (tipoFrete == 2):
        return 200
    else:
        return 0
        

# [EXIGÊNCIA DE CÓDIGO 1 de 7];
print('Bem-vindo a Fábrica de Camisas do Jéferson Diego Leidemer\n')

print('MCS - Manga Curta Simples: R$1.80 cada')
print('MLS - Manga Longa Simples: R$2.10 cada')
print('MCE - Manga Curta Com Estampa: R$2.90 cada')
print('MLE - Manga Longa Com Estampa: R$3.20 cada')

# Modelo de camiseta
modeloEscolhido = escolha_modelo()

# Quantide de camisetas
qtdComDesconto = num_camisetas()

print('1 - Transportadora - R$100.00')
print('2 - Sedex - R$200.00')
print('0 - Retirar na fábrica - R$0.00')

# Frete
valorFrete = frete()

# [EXIGÊNCIA DE CÓDIGO 5 de 7]
#Total
total = (modeloEscolhido * qtdComDesconto) + valorFrete

# Finalização
print('Total: R${0:.2f} (Modelo: {1:.2f} * Quantidade(com desconto): {2:.0f} + frete: {3:.2f}'.format(total, modeloEscolhido, qtdComDesconto, valorFrete))