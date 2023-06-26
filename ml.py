import requests
import json
print('*' * 45)
print('Código Mercado Livre')
print('*' * 45)
print('Cole o link do Anúncio no Mercado Livre \n')
link = input('Link: ')
print('')


if 'https://' in link:
    link = link.replace('https://', '')
elif 'http://' in link:
    link = link.replace('http://', '')

link = link.replace('produto.mercadolivre.com.br/', '')
link = link[:15]
link = link.replace('-','')
api = f'https://api.mercadolibre.com/items/{link}'

response = requests.get(api)
html = response.text

data = json.loads(html)
category_id = data['category_id']

print('O Category_ID desse anuncio é: \n')
print(category_id)
