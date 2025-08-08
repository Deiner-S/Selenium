from selenium import webdriver
from selenium.webdriver.common.by import By
from extraction_pages import ExtractionPages as ep
import time
import pandas as pd




driver = webdriver.Chrome()
driver.get("https://fau.softcomshop.com.br/auth/login")

input_login = driver.find_element(By.CSS_SELECTOR, "#login-email")
input_senha = element = driver.find_element(By.CSS_SELECTOR, "#login-senha")
button_login = driver.find_element(By.CSS_SELECTOR, "#login-acessar")

login = ""
input_login.send_keys(login)

senha = ""
input_senha.send_keys(senha)

button_login.click()

driver.implicitly_wait(5)

lista = []

for indice in range(462,463):
    try:
        extract = ep()
        driver.get(f"https://fau.softcomshop.com.br/nfe2/{indice}/editar")
        
        extract.removpopup(driver)
        extract
        
        
        


        lista.append(dados)
    except Exception as e:
        with open("log.txt", "a", encoding="utf-8") as log:
            log.writelines(f"Erro: {str(e)}")
        print("não foi possível")
print(lista)
#df = pd.DataFrame(lista)
#df.to_csv("Relatorio_financeiro.csv")

driver.quit()
