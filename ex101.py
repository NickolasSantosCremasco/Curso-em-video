def voto(ano):
    if ano < 16:
        votar = 18 - ano
        print(f'O usuário tem {ano} anos, por tanto só podera votar em {votar} anos')
    if ano == 16 or ano == 17:
        print(f'O usuario tem {ano} anos, por tanto seu voto é opcional')
    if ano >= 18:
        print(f'O usuário tem {ano} anos por tanto seu voto é obrigatorio')

idade = int(input('Digite sua idade: '))
voto(idade)
