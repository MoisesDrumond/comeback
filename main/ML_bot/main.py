import sys
from pathlib import Path
from time import sleep
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Criação do navegador — simplificado sem Service nem chromedriver manual
def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')

    if options:
        for option in options:
            chrome_options.add_argument(option)

    browser = webdriver.Chrome(options=chrome_options)
    return browser

# Função para capturar screenshots em caso de erro
def salvar_screenshot(browser, nome='screenshot'):
    timestamp = datetime.now().strftime('%Y-%m-%d%H-%M-%S')
    filename = f'{nome}_{timestamp}.png'
    browser.save_screenshot(filename)
    print(f'[🖼️] Screenshot salva: {filename}')

# Função principal de ativar produtos da página
def ativar_produtos_na_pagina(browser, timeout=15) -> bool:
    wait = WebDriverWait(browser, timeout)

    try:
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-testid="active-listing-container"]')
        ))
    except Exception:
        print('[⚠️] Nenhum produto encontrado na página.')
        return False

    produtos = browser.find_elements(By.CSS_SELECTOR, '[data-testid="active-listing-container"]')

    if not produtos:
        print('[⚠️] Lista de produtos vazia.')
        return False

    print(f'[📦] {len(produtos)} produtos encontrados na página.')

    for index, produto in enumerate(produtos, start=1):
        try:
            status_element = produto.find_element(By.CSS_SELECTOR, '[data-testid="listing-status"]')
            status_text = status_element.text.strip().lower()

            nome_element = produto.find_element(By.CSS_SELECTOR, '[data-testid="listing-title"]')
            nome_produto = nome_element.text.strip()

            if status_text != 'ativo':
                print(f'[🛠️] Produto "{nome_produto}" ({index}) está INATIVO. Iniciando ativação...')

                menu_button = produto.find_element(By.CSS_SELECTOR, '[data-testid="overflow-menu-button"]')
                menu_button.click()
                sleep(0.5)

                editar_opcao = WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul[role="menu"] li'))
                )
                editar_opcao.click()

                browser.switch_to.window(browser.window_handles[-1])

                try:
                    ativar_button = WebDriverWait(browser, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Ativar")]'))
                    )
                    ativar_button.click()

                    try:
                        WebDriverWait(browser, 10).until(EC.invisibility_of_element(ativar_button))
                        print(f'[✅] Produto "{nome_produto}" ativado com sucesso!')
                    except:
                        sleep(2)
                        print(f'[✅] Produto "{nome_produto}" ativado (fallback no sleep).')

                except Exception as e:
                    print(f'[❌] Erro ao ativar produto "{nome_produto}": {e}')
                    salvar_screenshot(browser, nome='erro_ativar')
                    raise

                finally:
                    browser.close()
                    browser.switch_to.window(browser.window_handles[0])
                    sleep(0.5)

            else:
                print(f'[✔️] Produto "{nome_produto}" ({index}) já está ATIVO.')

        except Exception as e:
            print(f'[⚠️] Erro no processamento do produto {index}: {e}')
            salvar_screenshot(browser, nome='erro_produto')
            continue

    return True

# Avança para a próxima página
def avancar_pagina(browser, timeout=10) -> bool:
    try:
        wait = WebDriverWait(browser, timeout)
        botao_proxima = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.pagination__next a'))
        )
        botao_proxima.click()

        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-testid="active-listing-container"]')
        ))
        print('[➡️] Avançando para a próxima página...')
        return True

    except Exception:
        print('[❌] Não há mais páginas para avançar.')
        return False

# Função para acessar os anúncios inativos (apenas o primeiro link)
def acessar_anuncios_inativos(browser):
    url = 'https://www.mercadolivre.com.br/anuncios/lista?filters=OMNI_UNDER_REVIEW&loadSession=1&page=1&sort=DEFAULT&task=MODERATE_MARKETPLACE'

    print(f'[🌐] Tentando acessar: {url}')
    browser.get(url)
    sleep(3)

    try:
        # Verifica se o conteúdo relevante foi carregado
        browser.find_element(By.CSS_SELECTOR, '[data-testid="active-listing-container"]')
        print('[✅] Página carregada com sucesso!')
        return True  # Se a página foi carregada corretamente, retorna True
    except Exception as e:
        print(f'[❌] Não carregou. Erro: {e}')
        return False

# Função principal
def navegar_e_ativar():
    browser = make_chrome_browser()

    try:
        browser.get('https://www.mercadolivre.com.br/')
        print('[🌐] Acesse o Mercado Livre e faça o login.')

        input('⚠️ Após fazer login manualmente, pressione ENTER para continuar...')

        if not acessar_anuncios_inativos(browser):
            print('[❌] Não foi possível acessar a página de anúncios inativos.')
            return

        while True:
            encontrou = ativar_produtos_na_pagina(browser)

            if not encontrou:
                print('[ℹ️] Nenhum produto encontrado na página.')

            if not avancar_pagina(browser):
                break

    finally:
        input('\n🛑 Processo finalizado. Pressione ENTER para fechar...')
        browser.quit()

if __name__ == '__main__':
    navegar_e_ativar()
