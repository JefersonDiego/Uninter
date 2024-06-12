# Exercício 1
# Desenvolva um algoritmoo que solicite ao usuário o preço de um produto
# e um percentual de desconto a ser aplicado a ele. Calcule e exiba o
# valor do desconto e o preço final do produto.
'''
preco_produto = float(input('Digite o preço do seu produto: R$'))
percentual_desconto = float(input('Digite o percentual de desconto (0 - 100%):    %\b\b\b\b'))

valor_desconto = (preco_produto * percentual_desconto) / 100
preco_final = preco_produto - valor_desconto

print('O valor do seu desconto é de R${}'.format(valor_desconto))
print('O preço final do seu produto é de R${}'.format(preco_final))
'''


#Exercício 2
# Escreva um programa que pergunte a quantidade de km percorridos por uma carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

valor_km = 0.15
km_percorridos = int(input('Km percorridos no total: '))
valor_total_km = km_percorridos * valor_km

valor_diaria = 60
diarias = int(input('Total de dias com o carro: '))
diarias_totais = diarias * valor_diaria

total_pagar = valor_total_km + diarias_totais
print('O valor total da diária é de R${}.\nO valor total pelos km percorridos é de {}.\nO valor total da locação é de R${}.'.format(diarias_totais, valor_total_km, total_pagar))