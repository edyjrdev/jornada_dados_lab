import requests
from bs4 import BeautifulSoup
import pandas as pd

from dataclasses import dataclass 

@dataclass
class Produto:
    titulo: str
    classificao: str
    preco_atual_int: str

# https://lista.mercadolivre.com.br/xiaomi-15t-pro



produto = 'xiomi-15t-pro' 

# header para driblar ML
headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)'"}

url = f'https://lista.mercadolivre.com.br/{produto}' # Pesquisa Mercado Livre

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # print(response.json())
    soup = BeautifulSoup(response.text, 'html.parser')  # retorna html (estrutura do site)
    # print(soup.prettify())

    lista_produtos = soup.find_all("li", class_="ui-search-layout__item")
    lista_dados = []

    for i, produto in enumerate(lista_produtos, start=1):
        titulo = produto.find("a", class_="poly-component__title").text
        classificao = produto.find('span', class_='poly-phrase-label')
        if classificao:
            classificao = classificao.text
        else:
            classificao = '0'
       
        preco_atual_int = produto.find('span', class_="andes-money-amount__fraction").text
        #  print(i, titulo , classificao, preco_atual_int, sep='|')
        prod = Produto(titulo, classificao, preco_atual_int)
        lista_dados.append(prod)
else:
    print(response.status_code, 'Erro')

print(len(lista_dados))
for i in lista_dados:
    print(i)