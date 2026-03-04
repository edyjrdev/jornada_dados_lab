import requests
from bs4 import BeautifulSoup


url_login = 'https://www.codechef.com/api/codechef/login'
url_dashboard = 'https://www.codechef.com/dashboard'

"""
Form Login name, pass, submit e:
<input type="hidden" name="csrfToken" id="edit-csrfToken" 
value="9a383c9d71148a941d321ebe3d08e2120a8dd489420315fef3957247d578391f" 
autocomplete="none">
"""

#login payload
payload = {
    'name':'edyjrdev@gmail.com',
    'pass':'secret',
    'form_id': 'ajax_login_form'
}


with requests.Session() as session:
    # 1 Chamada para Gerar Token
    response = session.get(url_login)

    # Pegar HTML para acessar token gerado
    context = session.get(url_login)
    soup = BeautifulSoup(context.text, 'html.parser')

    """
    # Procurar input do token e do idform
    inputs = soup.find_all('input')  # procurar inputs
    for input in inputs:
        print(input['name']) # r'\"csrfToken\"' e r'\"form_build_id\"'
    """
    nome = r'\"csrfToken\"'

    token = soup.find('input', {'name': nome})
    token_valor = token.get('value')
    token_cleanned = token_valor.replace(r'\"', '')
    print(token_valor,'->', token_cleanned)
    
    form = r'\"form_build_id\"'
    form_id = soup.find('input', {'name': form})
    form_id_valor = form_id.get('value')
    form_id_cleanned = form_id_valor.replace(r'\"', '')
    print(form_id_valor, '->', form_id_cleanned)
    
    #Adicionar token e form_id ao payload
    payload['csrfToken'] = token_cleanned
    payload['form_build_id'] = form_id_cleanned

    print(payload)

    login = session.post(url_login, data=payload)
    
    match login.status_code:
        case 200:
            print(login.json())  # {'status': 'success', 'success': 'Redirecting...', 'redirect': '/dashboard'}
            dashboard = session.get(url_dashboard)
            
            match dashboard.status_code:
                case 200:
                    print(dashboard.content)
        case 400:
            print(login.json())
            
        case _:
            print(login.status_code, 'Erro')
            