#Código para ver se o site pudim está acessível

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('ERRO! o site pudim  ão está acessível no momento. ')
else:
    print('O site está acessível')
    print(site.read())