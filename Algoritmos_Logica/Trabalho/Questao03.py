def valida_modelo():
    while True:
        try:
            modelo = input().lower()
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


def escolha_modelo(modelo):
    if (modelo == 'mcs'):
        return 1.8
    elif (modelo == 'mls'):
        return 2.1
    elif (modelo == 'mce'):
        return 2.0
    elif (modelo == 'mle'):
        return 3.2

def num_camisetas(qtd):
    if ((qtd >= 20) and (qtd < 200)):
        return (qtd - (qtd * 0.05))
    elif ((qtd >= 200) and (qtd < 2000)):
        return (qtd - (qtd * 0.07))
    elif ((qtd >= 20000) and (qtd < 20000)):
        return (qtd - (qtd * 0.12))
    else:
        return qtd


print('Bem-vindo a Fábrica de Camisas do Jéferson Diego Leidemer\n')
print('Entre com o modelo desejado: ')
print('MCS - Manga Curta Simples: R$1.80 cada')
print('MLS - Manga Longa Simples: R$2.10 cada')
print('MCE - Manga Curta Com Estampa: R$2.90 cada')
print('MLE - Manga Longa Com Estampa: R$3.20 cada')

modelo = valida_modelo()
modeloEscolhido = escolha_modelo(modelo)

qtdCamisetas = valida_qtd('Digite a quantidade de camisetas (entre 1 e 20000): ')
print('Valor: R${} '.format(modeloEscolhido * num_camisetas(qtdCamisetas)))

print(qtdCamisetas)