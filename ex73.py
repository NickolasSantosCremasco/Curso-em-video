print('Tabela do Brasileirão')
tabela = ('Palmeiras','Botafogo','Atletico-MG','Flamengo','Grêmio','Bragantino','Fluminense','Atletico-PR','São Paulo','Internacional','Fortaleza','Cuiabá','Corinthians','Cruzeiro','Santos','Vasco Da Gama','Bahia','Goiás','Coritiba','América-MG')
cont = 1
print('OS TIMES DE 1º A 5º SÃO: ')
for times in tabela[:5]:
    print(f'{cont}º - {times}')
    cont += 1
print('OS TIMES DE 17º A 20º SÃO: ')
cont = 17
for times in tabela[16:]:
    print(f'{cont}º - {times} ')
    cont += 1

cont = 1
print('OS TIMES EM ORDEM ALFABÉTICA FICAM: ')
for time in sorted(tabela):
    print(f'{cont}º - {time} ')
    cont += 1

cont = 0
botafogo = tabela.index('Botafogo')
cont = botafogo + 1
print(f'O Botafogo esta na {cont}º Posição ')