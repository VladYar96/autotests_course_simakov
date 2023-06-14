# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from pathlib import Path
import requests

driver = webdriver.Chrome()
action = ActionChains(driver)
path = Path.cwd()
sbis_site = 'https://sbis.ru/'


try:
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(5)
    footer = driver.find_element(By.CSS_SELECTOR, '.sbisru-Footer__container')
    driver.execute_script("return arguments[0].scrollIntoView(true);", footer)
    sleep(3)
    download_sbis = driver.find_element(By.CSS_SELECTOR, 'a[href="/download?tab=ereport&innerTab=ereport25"]')
    assert download_sbis.is_displayed(), 'Не найдена строка "Скачать СБИС"'
    download_txt = download_sbis.get_attribute('href')
    download_sbis.click()
    sleep(5)
    assert driver.current_url == download_txt, 'Перешли не на ту страницу'
    plugin = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    plugin.click()
    sleep(1)
    download_plugin = driver.find_elements(By.CSS_SELECTOR, '[data-for="plugin"] .sbis_ru-DownloadNew-loadLink a')[0]
    url_plugin = download_plugin.get_attribute('href')
    r = requests.get(url_plugin, allow_redirects=True)
    sleep(7)
    plugin_path = Path(path, 'sbisplugin-setup-web.exe')
    with open('sbisplugin-setup-web.exe', "wb") as code:
        code.write(r.content)
    assert plugin_path.is_file(), 'Плагин не скачался'
    size_plugin = plugin_path.stat().st_size
    print(f'Размер скачанного файла: {round(size_plugin / 1048576, 3)} Мегабайт')
finally:
    driver.quit()
