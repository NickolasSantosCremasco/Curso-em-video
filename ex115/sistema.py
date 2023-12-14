from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    sleep(1)
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #Listar o conteudo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)

    elif resposta == 3:
        cabecalho('SAINDO DO SISTEMA.... ATÉ LOGO! ')
        break
    else:
        print('\033[31m ERRO! Digite uma opção válida\033[m ')


