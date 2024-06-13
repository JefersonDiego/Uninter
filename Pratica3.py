# Exercícios de fixação

# Escreva as seguintes expressões booleanas em linguagem Python

# Somatório de 2 com 2 é menor que 4
print(2 + 2 < 4)

# O valor de 7 // 3 ée igual a 1 + 1
print(7 // 3 == 1 + 1)

# A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25
print(3**2 + 4**2 == 25)

# A soma de 2, 4 e 6 é maior que 12
print(2 + 4 + 6 > 12)

# 1387 é divisível por 19?
print(1387 % 19 == 0)

# 31 é par?
print(31%2 == 0)

# O menor valor entre 34, 29 e 31 é menor que 30?
print(min(34, 29, 31) < 30)

# Traduza as afirmações a seguir para condicionais em Python
# Se a idade é maior que 60, escreva: "Você tem diretio aos benefícios"
idade = 61
if (idade > 60):
    print('Você tem direito aos benefícios')
    
# Se dano é maior que 10 e escudo é igual a 0, escreve: "Você está morto"
dano = 11
escudo = 0
if (dano > 10 and escudo == 0):
    print('Você está morto')

# Se pelo menos uma das variáveis booleanas norte, sul, leste, oeste resultarem
# em True, escreva: "Você escapou!"

norte = 0
sul = 1
leste = 0
oeste = 0
if (norte or sul or leste or oeste):
    print('Você escapou!')

# Condicional composta
# Traduza as afirmações a seguir para condicionais em Python

# Se o ano é divisível por 4, escreva: "Pode ser um ano bissexto". Caso
# contrário, escreva: "Definitivamente não é um ano bissexto"

ano = 2001
if (ano % 4 == 0):
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')

# Se ambas as variáveis booleanas cima e baixo forem True, escreva:
# "Decida-se!". caso contrário, escreva: "Você escolheu um caminho!"

cima = 1
baixo = 0
if (cima and baixo):
    print('Decida-se')
else:
    print('Você escolheu um caminho!')