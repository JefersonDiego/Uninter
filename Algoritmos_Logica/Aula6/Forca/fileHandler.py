def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def abrirArquivoLeitura(nomeArquivo):
    try:
        a = open(nomeArquivo, 'r')
    except:
        print('Não foi possível abrir para leitura.')
    else:
        print('Arquivo {} aberto com sucesso"\n'.format(nomeArquivo))
        return a

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print('Arquivo {} criado com sucuesso!\n'.format(nomeArquivo))

def listaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else: # se deu certo
        dados = a.readlines()
    finally: # listando ou não
        a.close()
        return dados

def inserir_score(nomeArquivo, nomeJogador, score):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write('{};{}\n'.format(nomeJogador, score))
    finally:
        a.close