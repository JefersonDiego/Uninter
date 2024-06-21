# Texto do menu principal
def imprime_menu_principal():
    print()
    print('MENU')
    print('1) Cadastrar Funcionário')
    print('2) Consultar Funcionário')
    print('3) Remover Funcionário')
    print('4) Encerrar Programa')
    
    return valida_opcao('Escolha uma das opções: ')

# Texto do menu consulta
def imprime_menu_consulta():
    print()
    print('2) Consultar Funcionário')
    print('    1. Consultar Todos')
    print('    2. Consultar por Id')
    print('    3. Consultar por Setor')
    print('    4. Retornar ao menu')
    
    return valida_opcao('Escolha uma das opções: ')

# Testa se a opção selecionada nos menus é válida
def valida_opcao(pergunta):
    while True:
        try:
            opcao = int(input(pergunta))
            if (opcao >= 1) and (opcao <= 4):
                return opcao
            else:
                print('Opção inválida. Tente novamente.')
        except:
            print('Valor não reconhecido.')

# Testa se os campos, como nome, são string
def valida_string(pergunta):
    while True:
        try:
            palavra = input(pergunta)
            teste = int(palavra) # Se pode ser convertido para inteiro, não é string, não retorna erro
            print('Você deve digitar somente palavras.')
        except:
            try:
                teste = float(palavra) # Se pode ser convertido para real, não é string, não retorna erro
                print('Você deve digitar somente palavras.')
            except ValueError:
                return palavra # Nesse caso, queremos que ocorra um erro, pois se ocorrrer erro, é uma string
                               # [EXIGÊNCIA DE CÓDIGO 8 de 8];
                               
# Validação para que o salário seja um número positivo, maior que 0
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
    print('\nCADASTRAR')
    cadastro['id'] = id
    print('Id do funcionário: {}'.format(id))
    cadastro['nome'] = valida_string('Digite o nome do funcionário: ') # Deve ser somente string
    cadastro['setor'] = input('Digite o setor do funcionário: ') # pode ser qualquer coisa
    cadastro['salario'] = valida_salario('Digite o salário do funcionário: ') # Deve ser número positivo maior que zero
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
    print('-' * 30)


# Testa se a ID é um número válido e se existe no cadastro
def valida_id(lista_func, pergunta):
    while True:
        try:            
            id = int(input(pergunta))
            if id > 0:
                for keys in lista_func:
                    if keys['id'] == id:
                        return id
                print('ID não encontrada.')
            elif (id < 0):
                print('Digite um valor maior do que 0.')
            else:
                return 0
        except ValueError:
            print('ID deve ser um número inteiro.')

# Imprime a busca por uma chave específica na tela, recebe a chave(busca) e o valor(item) a ser buscado
def imprime_consulta(busca, item, lista_func):
    print('-' * 30)
    for func in lista_func:
        for chave, valor in func.items():
            if (chave == busca) and (valor == item):
                for i, j in func.items():
                    print('{}: {}'.format(i, j))
                print()
    print('-' * 30)
    return 0

# Cria um laço para que se possa fazer várias buscas pela ID seguidas        
def consulta_id(lista_func):
    while True:
        id_consulta = valida_id(lista_func, 'Informe uma ID para consultar ou 0 para sair: ')
        if id_consulta == 0:
            return
        id_consulta = imprime_consulta('id', id_consulta, lista_func)


# Validação para verificar a existência do setor no cadastro
def valida_setor(lista_func):
    while True:
        try:            
            setor = input('Informe o setor a ser consultado ou 0 para sair: ')
            if setor != '0':
                for keys in lista_func:
                    if keys['setor'] == setor:
                        return setor
                print('Setor não encontrado.')
            else:
                return 0
        except ValueError:
            print('Valor não reconhecido.')

# Cria um laço para que se possa fazer várias buscas pelo setor seguidas 
def consulta_setor(lista_func):
    while True:
        setor_consulta = valida_setor(lista_func)
        if setor_consulta == 0:
            return
        setor_consulta = imprime_consulta('setor', setor_consulta, lista_func)

def remove_funcionario(lista_func): # [EXIGÊNCIA DE CÓDIGO 5 de 8]
    item = valida_id(lista_func, 'Informe a ID do funcionário ser removido ou 0 para sair: ')
    for i in range(len(lista_func)):
        if lista_func[i]['id'] == item:
            del lista_func[i]
            print('Funcionário removido.')
            return lista_func

lista_funcionarios = [{'id':4901955, 'nome':'Nome1', 'setor':'setor1', 'salario':1001},
                      {'id':4901956, 'nome':'Nome2', 'setor':'setor1', 'salario':1002},
                      {'id':4901957, 'nome':'Nome3', 'setor':'setor3', 'salario':1003},
                      {'id':4901958, 'nome':'Nome4', 'setor':'setor1', 'salario':1004}]

lista_funcionarios = []

id_global = 4901954 # [EXIGÊNCIA DE CÓDIGO 2 de 8]

print('Bem-vindos a empresa do Jéferson Diego Leidemer') # [EXIGÊNCIA DE CÓDIGO 1 de 8]

opcao = imprime_menu_principal()
while True: # [EXIGÊNCIA DE CÓDIGO 6 de 8]
    match opcao:
        case 1: # Cadastrar
            id_global += 1
            lista_funcionarios = cadastrar_funcionario(id_global, lista_funcionarios) # [EXIGÊNCIA DE CÓDIGO 7 de 8]
            opcao = imprime_menu_principal()
            continue
        case 2: # Consultar
            consultar_funcionarios(lista_funcionarios)
            opcao = imprime_menu_principal()
            continue
        case 3: # Remover
            lista_funcionarios = remove_funcionario(lista_funcionarios)
            opcao = imprime_menu_principal()
            continue
        case 4:
            print('Saindo...')
            break
        case _:
            continue