import requests

def navegador(url):
    try:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36'})
        codigo = res.status_code
    except:
        codigo = 500
    if codigo == 200:
        mensagem = f'url: {url} executado com sucesso!'
    else:
        mensagem = f'url: {url} falhou!'
    print(mensagem)

def rodar_rotinas():
    navegador('https://rotina.joelsilva3.repl.co/')
    navegador('https://telegram.joelsilva3.repl.co/')
    navegador('https://statistic.joelsilva3.repl.co/')
    navegador('https://painel.joelsilva3.repl.co/')
    navegador('https://painel.antonio-carlo22.repl.co/')
    navegador('https://apiresolver.joelsilva3.repl.co/')
    

rodar_rotinas()
