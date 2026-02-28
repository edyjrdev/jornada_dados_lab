from curl_cffi import requests
import time

# Classe de Raspador do Pao de Açucar
class PaoDeAcucarScraper:
    def __init__(self, pesquisa='azeite'):
        self.origin = 'https://www.paodeacucar.com'
        self.referer = 'https://www.paodeacucar.com/'
        self.products = []  # lista de produtos
        self.page = 1
        self.totalPages = 0
        self.resultsPerPage = 48
        self.pesquisa = pesquisa
        # Estrategia de Retry
        self.max_retries = 4
        self.status_codes_retry = [404, 429,500,502,503,504]

        # 1. Initialize a session to manage cookies automatically
        self.session = requests.Session()
        # 2. Visit the main search page first to "prime" the session
        # This mimics a real user landing on the site
        base_url = f"https://www.paodeacucar.com/busca?terms={self.pesquisa}"
        
        prime_headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        }

        # Impersonate chrome to bypass TLS fingerprinting
        self.session.get(base_url, headers=prime_headers, impersonate="chrome")

        self.api_headers = {
            "authority": "api.vendas.gpa.digital",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": "https://www.paodeacucar.com",
            "referer": "https://www.paodeacucar.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        }
        self.api_endpoint = "https://api.vendas.gpa.digital/pa/search/search"
        self.payload = {
            "terms": self.pesquisa,
            "page": self.page,
            "sortBy": "relevance",
            "resultsPerPage": self.resultsPerPage,
            "allowRedirect": True,
            "storeId": 461,
            "department": "ecom",
            "customerPlus": True,
            "partner": "fallback"
        }
        self.get_total_pages()

    # Gemini montou essa estrategia de retry
    # curl_cffi nao tem Retry nem HTTPAdapater
    def request_with_retry(self, method, url, **kwargs):
        for attempt in range(self.max_retries):
            response = self.session.request(method, url, **kwargs)
            # Estrategia de retry
            if response.status_code in self.status_codes_retry:
                time.sleep(2 ** attempt)  # Exponential backoff
                continue
            return response
        return response

    def get_total_pages(self):
        response = self.request_with_retry(
            "POST",
            self.api_endpoint, 
            headers=self.api_headers, 
            json=self.payload, 
            impersonate="chrome"
        )

        if response.status_code == 200:
            # Achei todas paginas para paginar
            json = response.json()
            self.totalPages = json.get('totalPages')
            print(f'Pesquisa por:  {self.pesquisa}')
            print(f'Total de Paginas: {self.totalPages}')
            pagina_produtos = json.get('products')
            for prod in pagina_produtos:
                self.products.append(prod)
            self.get_products()  # buscar demais paginas
        else:
            print(f"Error {response.status_code}: {response.text}")

    def get_products(self):
        for i in range(2, self.totalPages -1):

            self.payload = {
                "terms": self.pesquisa,
                "page": i,
                "sortBy": "relevance",
                "resultsPerPage": self.resultsPerPage,
                "allowRedirect": True,
                "storeId": 461,
                "department": "ecom",
                "customerPlus": True,
                "partner": "fallback"
            }

            response = self.request_with_retry(
                      "POST",
                      self.api_endpoint, 
                      headers=self.api_headers, 
                      json=self.payload, 
                      impersonate="chrome"
            )

            if response.status_code == 200:
                json = response.json()
                produts = json.get('products')
                print(f'Baixando pagina {i} com {len(produts)}')
                pagina_produtos = json.get('products')
                for prod in pagina_produtos:
                    self.products.append(prod)
            else:
                print(f"Erro na pagina {i} - {response.status_code}: {response.text}")
        return self.products

# Execution
prods = PaoDeAcucarScraper('coco').products

if prods:
    for n, prod in enumerate(prods, start=1):
        id = None
        nome = None
        marca = None
        preco = None
        for key in prod.keys():
            match key: 
                case 'id':
                    id = prod["id"]
                case 'name':
                    nome = prod["name"]
                case 'price':
                    preco = prod["price"]
                case 'brand':
                    marca = prod["brand"]
        
        print(f'{n} | id:{id} | nome:{nome} | marca:{marca} | preço:{preco if preco else 0}')