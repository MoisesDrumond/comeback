# type: ignore
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

    chrome_options.add_argument('--start-maximized')

    if options:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(CHROME_DRIVER_PATH))
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser


def ativar_produtos_na_pagina(browser: webdriver.Chrome, timeout=15):
    wait = WebDriverWait(browser, timeout)

    sleep(2)  # Pequeno delay para garantir que a página carregou

    produtos = browser.find_elements(By.CSS_SELECTOR, 'div.listing-item')  # Ajuste esse seletor para o correto

    print(f'Encontrados {len(produtos)} produtos nesta página.')

    for produto in produtos:
        try:
            # Verificar se está inativo (ajustar seletor certo de acordo com a indicação de inativo)
            status = produto.find_element(By.CSS_SELECTOR, '.status-tag').text.lower()

            if 'inativo' in status:
                print('Produto inativo encontrado. Iniciando processo de ativação.')

                # Clicar no menu de opções (botão overflow ⋮)
                menu = produto.find_element(By.CSS_SELECTOR, 'button.dropdown-trigger')
                menu.click()

                sleep(1)

                # Clicar com botão direito na primeira opção
                primeira_opcao = produto.find_element(By.CSS_SELECTOR, 'ul.dropdown-menu li:nth-child(1)')
                webdriver.ActionChains(browser).context_click(primeira_opcao).perform()

                sleep(1)

                # Clicar na primeira opção que surge no menu do clique direito
                subopcao = produto.find_element(By.CSS_SELECTOR, 'ul.context-menu li:nth-child(1)')
                subopcao.click()

                sleep(2)  # Esperar nova aba abrir

                # Trocar para a nova aba
                browser.switch_to.window(browser.window_handles[-1])

                # Clicar no botão 'Ativar'
                ativar_btn = wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Ativar")]'))
                )
                ativar_btn.click()

                print('Produto ativado com sucesso.')

                sleep(2)

                # Fechar a aba atual e voltar para a lista
                browser.close()
                browser.switch_to.window(browser.window_handles[0])

                sleep(1)

        except Exception as e:
            print(f'Erro ao processar um produto: {e}')
            continue


def avancar_pagina(browser: webdriver.Chrome, timeout=10) -> bool:
    try:
        wait = WebDriverWait(browser, timeout)
        botao_proxima = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.andes-pagination__link--next'))
        )
        botao_proxima.click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.listing-item')))
        print('Avançando para a próxima página...')
        return True
    except Exception as e:
        print(f'Não há próxima página. Encerrando loop. {e}')
        return False


def navegar_mercado_livre():
    options = ()  # Pode colocar '--headless' se quiser rodar sem abrir janela
    browser = make_chrome_browser(*options)

    try:
        # 🔗 Coloque aqui o link da sua aba de produtos do Mercado Livre
        browser.get('https://www.mercadolivre.com.br/')

        input('Faça login manualmente e pressione ENTER para continuar...')

        primeira_pagina = True

        while True:
            ativar_produtos_na_pagina(browser)

            if not avancar_pagina(browser):
                print('Processo concluído! Nenhuma página restante.')
                break

            primeira_pagina = False

    finally:
        input('\nPressione ENTER para fechar o navegador...')
        browser.quit()


if __name__ == '__main__':
    navegar_mercado_livre()
