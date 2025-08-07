from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
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

for indice in range(424,463):
    try:
        driver.get(f"https://fau.softcomshop.com.br/nfe2/{indice}/editar")
        
        try:
            button_not_show = driver.find_element(By.CSS_SELECTOR, ".content-do-not-show-button")
            button_not_show.click()
        except Exception as e:
            with open("log.txt", "a", encoding="utf-8") as log:
                log.writelines(f"Erro: {str(e)}")
            print ("Botão não encontrado")
        
        html = driver.page_source
        
        soup = BeautifulSoup(html,"html.parser")

        dados = {
        "chave_nota" : soup.find("span", class_="access_key_nfe").text,
        "numero da nota" : soup.find("span", class_="number_nfe").text,
        "cpf" : soup.find("input", class_="form-control mask_cpf_cnpj")["value"],
        "valor da nota": soup.find("span", id="total_produto_valor").text,
        "CFOP":soup.find("input", id="auto_natureza")["value"]}

        lista.append(dados)
    except Exception as e:
        with open("log.txt", "a", encoding="utf-8") as log:
            log.writelines(f"Erro: {str(e)}")
        print("não foi possível")

df = pd.DataFrame(lista)
df.to_csv("Relatorio_financeiro.csv")

driver.quit()

