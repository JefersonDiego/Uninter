print('Escolha o que deseja comprar:')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Digite uma opção: '))
qtd = int(input('Quantas unidades?'))

match (produto):
    case 1:
        pagar = qtd * 2.3
        print('Você comprou {} maçãs.'.format(qtd), end =' ')
        print('Total à pagar: R${0:.3g}'.format(pagar))
    case 2:
        pagar = qtd * 3.6
        print('Você comprou {} laranjas.'.format(qtd), end =' ')
        print('Total à pagar: R${0:.3g}'.format(pagar))
    case 3:
        pagar = qtd * 1.85
        print('Você comprou {} bananas.'.format(qtd), end =' ')
        print('Total à pagar: R${0:.3g}'.format(pagar))
    case _:
        print('produto não existe!')