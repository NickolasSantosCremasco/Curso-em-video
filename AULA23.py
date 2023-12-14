#TRATAMENTOS DE ERROS E EXCEÇÕES
#Erros acontecem
 #erro semântico a variavel não foi definida
 #erro sintatico a palavra não foi bem escrita

try:
    #Tente realizar esse código
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b

except (ValueError, TypeError):
    # se der errado faça isso
    print('Podem existir varios exceptions para vários tipos de erros, depois ver as exceptions que normalmente ocorrem em python')
    print(f'Tivemos um problema com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print(f'Não é possivel dividir um número por zero')
except KeyboardInterrupt:
    print(f'O usuário preferiu não informar os dados!')
except Exception as erro:
    #Se eu não for nenhum dos problemas que ocorreram acima mostrar ual tipo de exceção ocorreu no programa

    print(f'Infelizmente ocorreu um problema')
    print(f'O problema encontrado foi {erro.__class__}')
else:
    #Se deu certo faça isso
    print(f'O resultado é {r:.1f}')

finally:
    #mesmo que de certo ou errado iso vai ocorrer
    print(f'Volte sempre! Muito obrigado! ')