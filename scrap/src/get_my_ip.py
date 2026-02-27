import requests


# Retorna IP e Localização
"""
{'ip_version': 4, 'country': 'BR', 'asn': {'asnum': 28227, 'org_name': 'NOVACIA TECNOLOGIA E TELECOMUNICACOES LTDA'}, 'geo': {'city': 'Brasília', 'region': 'DF', 'region_name': 'Federal District', 'postal_code': '70640', 'latitude': -15.7798, 'longitude': -47.9331, 'tz': 'America/Sao_Paulo', 'lum_city': 'brasilia', 'lum_region': 'df'}}
"""
# url = 'http://lumtest.com/myip.json'

url = 'http://www.globo.com'

respose = requests.get(url)

if respose.status_code == 200:
    print(respose.json())
else:
    print(respose.status_code, 'Erro')