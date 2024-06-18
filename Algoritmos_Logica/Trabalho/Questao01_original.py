juros = 0

# inicia o algoritmo requsitanto o valor do pedido e valor da parcela
print ('Bem-vindo a loja do Jéferson Diego Leidemer!')
valorDoPedido = float(input('Informe o valor do pedido: R$'))
qtdParcelas = int(input('Informe a quantidade de parcelas: '))

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
