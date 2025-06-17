#type: ignore
from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # Abre o navegador maximizado
    chrome_options.add_argument('--start-maximized')

    if options:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(CHROME_DRIVER_PATH))
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser

def buscar_ak47(browser, timeout=10, primeira_pagina=True):
    wait = WebDriverWait(browser, timeout)

    # Apenas na primeira página: clicar em "Ver todos"
    if primeira_pagina:
        try:
            ver_todos_btn = wait.until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Ver todos'))
            )
            ver_todos_btn.click()
            wait.until(EC.presence_of_element_located((By.ID, 'searchResultsRows')))
            print('Clicou em "Ver todos".')
        except Exception:
            print('Botão "Ver todos" não encontrado ou já expandido.')

    else:
        # Aguarda o carregamento da nova página
        wait.until(EC.presence_of_element_located((By.ID, 'searchResultsRows')))

    # Verifica se há itens AK-47
    itens_ak = browser.find_elements(By.XPATH, '//a[contains(.,"AK-47")]')
    if itens_ak:
        print(f'Encontrado {len(itens_ak)} item(s) AK-47.')
        itens_ak[0].click()
        return True
    else:
        print('Nenhum item AK-47 encontrado nesta página.')
        return False

def avancar_pagina(browser, timeout=10):
    try:
        wait = WebDriverWait(browser, timeout)
        botao_proxima = wait.until(
            EC.element_to_be_clickable((By.ID, 'searchResults_btn_next'))
        )
        botao_proxima.click()

        wait.until(EC.presence_of_element_located((By.ID, 'searchResultsRows')))
        print('Avançando para a próxima página...')
        return True
    except Exception as e:
        print(f'Erro ao avançar para próxima página: {e}')
        return False

def navegar_mercado():
    options = ()  # Interface gráfica ativada
    browser = make_chrome_browser(*options)

    try:
        browser.get('https://steamcommunity.com/market/?l=brazilian')
        sleep(3)

        primeira_pagina = True

        while True:
            encontrou = buscar_ak47(browser, primeira_pagina=primeira_pagina)
            if encontrou:
                print('Item AK-47 encontrado e acessado!')
                break

            if not avancar_pagina(browser):
                print('Não foi possível encontrar mais páginas. Encerrando busca.')
                break

            primeira_pagina = False  # A partir daqui, não tenta mais clicar em "Ver todos"

    finally:
        input('\nPressione ENTER para fechar o navegador...')
        browser.quit()

if __name__ == '__main__':
    navegar_mercado()
