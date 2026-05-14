from requests import get

chave = 'fca6352b16e4b0407b22f6c98d9ae283'

def temperatura(cidade):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}&units=metric&lang=pt_br'
        resposta = get(url)
        dados = resposta.json()
        if dados['cod'] == 404:
            return f'Não encontrei a cidade {cidade}. Fale novamente um nome de alguma cidade que queira saber o clima.'
        
        temp = round(dados['main']['temp'])  
        sensacao = round(dados['main']['feels_like'])  
        umidade = dados['main']['humidity'] 
        descricao = dados['weather'][0]['description']

        return f'Em {cidade} a temperatura é {temp} graus, sensação térmica de {sensacao} graus, umidade de {umidade} por cento e o céu está {descricao}'
    except:
        return f'Não consegui buscar o clima de {cidade}, tente novamente'