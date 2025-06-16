from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    # chrome_options.add_argument('--headless')  # headless comentado

    if options:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(CHROME_DRIVER_PATH))
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser


def simular_ativacao_na_pagina(browser, timeout=15) -> bool:
    wait = WebDriverWait(browser, timeout)

    try:
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-testid="active-listing-container"]')
        ))
    except Exception:
        return False

    produtos = browser.find_elements(By.CSS_SELECTOR, '[data-testid="active-listing-container"]')

    if not produtos:
        return False

    for produto in produtos:
        try:
            status_element = produto.find_element(By.CSS_SELECTOR, '[data-testid="listing-status"]')
            status_text = status_element.text.strip().lower()

            if status_text != 'ativo':
                menu_button = produto.find_element(By.CSS_SELECTOR, '[data-testid="overflow-menu-button"]')
                menu_button.click()
                sleep(0.5)

                editar_opcao = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul[role="menu"] li'))
                )
                editar_opcao.click()

                browser.switch_to.window(browser.window_handles[-1])

                # NÃO clica no botão "Ativar", só simula a espera
                print("Simulando ativação do produto (não clicando)...")
                sleep(2)

                browser.close()
                browser.switch_to.window(browser.window_handles[0])

                sleep(0.5)

            else:
                continue

        except Exception:
            continue

    return True


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
        return True

    except Exception:
        return False


def navegar_e_simular():
    browser = make_chrome_browser()

    try:
        browser.get('https://www.mercadolivre.com.br/anuncios/lista?page=1')
        input('⚠️ Faça login manualmente e pressione ENTER para continuar...')
        sleep(2)

        while True:
            encontrou = simular_ativacao_na_pagina(browser)
            if not encontrou:
                pass
            if not avancar_pagina(browser):
                break

    finally:
        input('\nSimulação finalizada. Pressione ENTER para fechar...')
        browser.quit()


if __name__ == '__main__':
    navegar_e_simular()
