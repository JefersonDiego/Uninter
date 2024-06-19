juros = 0

# inicia o algoritmo requsitanto o valor do pedido e valor da parcela
print ('Bem-vindo a loja do Jéferson Diego Leidemer!') #[EXIGÊNCIA DE CÓDIGO 1 de 6]
valorDoPedido = float(input('Informe o valor do pedido: R$')) # [EXIGÊNCIA DE CÓDIGO 2 de 6];
qtdParcelas = int(input('Informe a quantidade de parcelas: ')) # [EXIGÊNCIA DE CÓDIGO 2 de 6];

# atribui a variável juros a porcentagem de juros de acordo com o número de parcelas
# [EXIGÊNCIA DE CÓDIGO 5 de 6
if (qtdParcelas >= 4) and (qtdParcelas < 6): # [EXIGÊNCIA DE CÓDIGO 3 de 6];
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
valorDaParcela = (valorDoPedido * (1 + juros) / qtdParcelas) # [EXIGÊNCIA DE CÓDIGO 4 de 6]
print('O valor das parcelas é de R${0:.2f}'.format(valorDaParcela))
# 0:.2f dentro das chaves formata o valor de saída para duas casas decimais # [EXIGÊNCIA DE CÓDIGO 6 de 6];

# realiza o cálculo do valor total e imprime na tela
valorTotalParcelado = valorDaParcela * qtdParcelas # [EXIGÊNCIA DE CÓDIGO 4 de 6]
print('O valor total da sua compra é de R${0:.2f}'.format(valorTotalParcelado))
