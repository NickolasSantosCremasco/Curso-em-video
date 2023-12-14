def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida\033[m')
            return 0
            break

        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida\033[m')
            return 0
            break

        else:
            return n

n1 = leiaInt('Numero inteiro:  ')
n2 = leiaFloat('Numero Real: ')
print(f'O valor inteiro foi \033[32m{n1}\033[32m e o valor real foi {n2}')