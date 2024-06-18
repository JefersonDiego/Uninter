juros = 0

def validaPedido(pergunta):
    while True:
            try:
                pedido = float(input(pergunta))
                while ((pedido <= 0)): # valor informado precisa ser maior do que zero
                    pedido = float(input(pergunta))
                return pedido
            except:
                print('Valor não reconhecido.')
    # caso seja informado algum caractere diferente de número,
    # volta para o início do laço

def validaParcelas(pergunta):
    while True:
        try:  # parcela precisa ser um número inteiro
            parcela = int(input(pergunta))
            while ((parcela <= 0)):
                parcela = int(input(pergunta))
            return parcela
        except:
            print('Valor não reconhecido.')

# inicia o algoritmo requisitanto o valor do pedido e valor da parcela
print ('Bem-vindo a loja do Jéferson Diego Leidemer!')
valorDoPedido = validaPedido('Informe o valor do pedido: R$')
qtdParcelas = validaParcelas('Informe a quantidade de parcelas: ')

# atribui a variável juros a porcentagem de juros de acordo com o número de parcelas
if (qtdParcelas >= 4) and (qtdParcelas < 6):
    juros = 0.04
elif (qtdParcelas >= 6) and (qtdParcelas < 9):
    juros = 0.08
elif (qtdParcelas >= 9) and (qtdParcelas < 13):
    juros = 0.16
elif (qtdParcelas >= 13):
    juros = 0.32
else:
    juros = 0


# realiza o cálculo do valor da parcela e imprime na tela
valorDaParcela = (valorDoPedido * (1 + juros) / qtdParcelas)
print('O valor das parcelas é de R${0:.2f}'.format(valorDaParcela))
# 0:.2f dentro das chaves formata o valor de saída para duas casas decimais

# realiza o cálculo do valor total e imprime na tela
valorTotalParcelado = valorDaParcela * qtdParcelas
print('O valor total da sua compra é de R${0:.2f}'.format(valorTotalParcelado))