"""
O selenium possui 8 componentes básicos:
    1. iniciar seção com o navegador
    2. Agindo no navegador de internet
    3. Solicitando informação do navegador de internet
    4. Estabelecendo uma Estratégia de Espera
    5. Encontrando um elemento
    6. Agindo no elemento
    7. Solicitando informações do elemento
    8. Encerrando a sessão
"""
#    importações necessárias
from selenium import webdriver
from selenium.webdriver.common.by import By


#    1. iniciar seção com o navegador
driver = webdriver.Chrome()

#    2. Agindo no navegador de internet

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#    3. Solicitando informação do navegador de internet
title = driver.title

#    4. Estabelecendo uma Estratégia de Espera
"""Essa não é a forma mais eficiente de definir um tempo de espera, mas serve como exemplo"""
driver.implicitly_wait(5.0)

#    5. Encontrando um elemento
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#    6. Agindo no elemento
text_box.send_keys("Selenium")
submit_button.click()

#    7. Solicitando informações do elemento
message = driver.find_element(by=By.ID, value="message")
text = message.text

#    8. Encerrando a sessão
driver.quit()
