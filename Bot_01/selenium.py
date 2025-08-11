from selenium import webdriver
from selenium.webdriver.common.by import By
from extraction_pages import ExtractionPages as ep

import time
import pandas as pd




driver = webdriver.Chrome()
driver.get()



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
