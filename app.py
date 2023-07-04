import requests
import unidecode
from bs4 import BeautifulSoup as bs
url = 'https://g1.globo.com/'

resposta = requests.get(url)
html = bs(resposta.text, 'html.parser')

noticias = html.find_all(
    'div', {'class': 'feed-post'})

indexNoticia = 0
for noticia in noticias:
  indexNoticia = indexNoticia + 1
  resumo = noticia.find('div', {'class': 'feed-post-body-resumo'})
  titulo = noticia.find('a', {'class': 'feed-post-link'})
  print('Noticia {}:'.format(indexNoticia))
  print(unidecode.unidecode(titulo.text))
  if (resumo != None):
    print(unidecode.unidecode(resumo.text))
  print('\n')
