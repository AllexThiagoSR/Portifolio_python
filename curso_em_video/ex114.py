import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site pudim não está ecessível no momento')
else:
    print('Consegui acessar o site pudim com sucesso.')
    print(site.read())
