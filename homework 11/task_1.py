# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/'
driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(3)
    assert driver.current_url == sbis_site, f'Неверно открыт сайт'
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    contacts.click()
    sleep(2)
    logo_tensor = driver.find_element(By.CSS_SELECTOR, '#contacts_clients .sbisru-Contacts__logo-tensor')
    assert logo_tensor, 'Не отобразился баннер Тензор'
    logo_tensor.click()
    driver.switch_to.window(driver.window_handles[1])
    sleep(3)
    assert driver.current_url == tensor_site, f'Неверно открыт сайт, должен открыться {tensor_site}'
    news_block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    driver.execute_script("return arguments[0].scrollIntoView(true);", news_block)
    assert news_block.is_displayed(), 'блок новости "Сила в людях" не отобразился'
    assert news_block.text == 'Сила в людях', 'Не найден блок новости "Сила в людях"'
    sleep(5)
    about = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-link[href='/about']")
    about.click()
    assert driver.current_url == 'https://tensor.ru/about', 'Неверно открыт сайт'
    sleep(3)
finally:
    driver.quit()