def imprime_menu_principal():
    print('MENU')
    print('1) Cadastrar Funcionário')
    print('2) Consultar Funcionário')
    print('    1. Consultar Todos')
    print('    2. Consultar por Id')
    print('    3. Consultar por Setor')
    print('    4. Retornar ao menu')
    print('3) Remover Funcionário')
    print('4) Encerrar Programa')
    
    return valida_opcao('Escolha uma das opções: ')

def imprime_menu_consulta():
    print('2) Consultar Funcionário')
    print('    1. Consultar Todos')
    print('    2. Consultar por Id')
    print('    3. Consultar por Setor')
    print('    4. Retornar ao menu')
    
    return valida_opcao('Escolha uma das opções: ')


def valida_opcao(pergunta):
    while True:
        try:
            opcao = int(input(pergunta))
            if (opcao >= 1) or (opcao <= 4):
                return opcao
            else:
                print('Opção inválida. Tente novamente.')
        except:
            print('Valor não reconhecido.')

def valida_string(pergunta):
    while True:
        try:
            palavra = input(pergunta)
            teste = int(palavra)
            print('Você deve digitar somente palavras.')
        except:
            try:
                teste = float(palavra)
                print('Você deve digitar somente palavras.')
            except ValueError:
                return palavra

def valida_salario(pergunta):
    while True:
        try:
            salario = float(input(pergunta))
            if (salario > 0):
                return salario
            else:
                print('Salário precisa ser maior que zero.')
        except:
            print('Valor não reconhecido.')

def cadastrar_funcionario(id, lista_func): # [EXIGÊNCIA DE CÓDIGO 3 de 8]
    cadastro = {}
    cadastro['id'] = id
    cadastro['nome'] = valida_string('Digite o nome do funcionário: ')
    cadastro['setor'] = input('Digite o setor do funcionário: ')
    cadastro['salario'] = valida_salario('Digite o salário do funcionário: ')
    lista_func.append(cadastro.copy())
    return lista_func
    
def consultar_funcionarios(lista_func): # [EXIGÊNCIA DE CÓDIGO 4 de 8]
    while True:
        opcao = imprime_menu_consulta()
        match opcao:
            case 1:
                print('-' * 30)
                consulta_todos(lista_func)
                continue
            case 2:
                consulta_id(lista_func)
                continue
            case 3:
                consulta_setor(lista_func)
                continue
            case 4:
                return

def consulta_todos(lista_func):
    for cadastros in lista_func:
        for chave, valor in cadastros.items():
            print('{}: {}'.format(chave, valor))
        print()

def valida_id(lista_func):
    while True:
        try:            
            id = int(input('Informe uma ID a ser consultada ou 0 para sair: '))
            if id > 0:
                for keys in lista_func:
                    if keys['id'] == id:
                        return id
                print('ID não encontrada.')
            elif (id <0):
                print('Digite um valor maior do que 0.')
            else:
                return 0
        except ValueError:
            print('ID deve ser um número inteiro.')

def imprime_consulta(busca, item, lista):
    for func in lista:
        for chave, valor in func.items():
            if (chave == busca) and (valor == item):
                for i, j in func.items():
                    print('{}: {}'.format(i, j))
                print()
    return 0
        
def consulta_id(lista_func):
    while True:
        id_consulta = valida_id(lista_func)
        if id_consulta == 0:
            return
        id_consulta = imprime_consulta('id', id_consulta, lista_func)


def valida_setor(lista_func):
    while True:
        try:            
            setor = input('Informe o setor a ser consultada ou 0 para sair: ')
            if setor != '0':
                for keys in lista_func:
                    if keys['setor'] == setor:
                        return setor
                print('Setor não encontrado.')
            else:
                return 0
        except ValueError:
            print('Valor não reconhecido.')

def consulta_setor(lista_func):
    while True:
        setor_consulta = valida_setor(lista_func)
        if setor_consulta == 0:
            return
        setor_consulta = imprime_consulta('setor', setor_consulta, lista_func)


lista_funcionarios = [{'id':1, 'nome':'Nome1', 'setor':'setor1', 'salario':1001},
                      {'id':2, 'nome':'Nome2', 'setor':'setor1', 'salario':1002},
                      {'id':1, 'nome':'Nome3', 'setor':'setor3', 'salario':1003},
                      {'id':4, 'nome':'Nome4', 'setor':'setor1', 'salario':1004}]
id_global = 4901954 # [EXIGÊNCIA DE CÓDIGO 2 de 8]

print('Bem-vindos a empresa do Jéferson Diego Leidemer\n') # [EXIGÊNCIA DE CÓDIGO 1 de 8]


opcao = imprime_menu_principal()
while True:
    match opcao:
        case 1:
            lista_funcionarios.append(cadastrar_funcionario(5, lista_funcionarios))
            print(lista_funcionarios)
            opcao = imprime_menu_principal()
            continue
        case 2:
            consultar_funcionarios(lista_funcionarios)
            opcao = imprime_menu_principal()
            continue
        case 4:
            print('Saindo...')
            break
        case _:
            continue


# [{'nome': 'j1', 'videogame': 'vg1', 'ano': '1'}, {'nome': 'j2', 'videogame': 'vg2', 'ano': '2'}, {'nome': 'j3', 'videogame': 'vg3', 'ano': '3'}]