from ex115.lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')#Se o arquivo ja existir ele vai abrir o arquivo em "read text"
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #Se não existir ele vai criar um arquivo com wt+ o + serve para indicar para só criar se não existir "Write Text"
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')

    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome = 'desconhecido', idade = 0 ):
    try:
        a = open(arq, 'at') #esse até vai abrir o arquivo de texto a adicionar elementos "append text" tirando da sigla
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado com SUCESSO! ;)')