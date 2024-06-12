# Exercício 1
# Desenvolva um algoritmoo que solicite ao usuário o preço de um produto
# e um percentual de desconto a ser aplicado a ele. Calcule e exiba o
# valor do desconto e o preço final do produto.

preco_produto = float(input('Digite o preço do seu produto: R$'))
percentual_desconto = float(input('Digite o percentual de desconto (0 - 100%):    %\b\b\b\b'))

valor_desconto = (preco_produto * percentual_desconto) / 100
preco_final = preco_produto - valor_desconto

print('O valor do seu desconto é de R${}'.format(valor_desconto))
print('O preço final do seu produto é de R${}'.format(preco_final))