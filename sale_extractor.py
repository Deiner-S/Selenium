from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import numpy as np
import time


class SaleExtractor():
    def __init__(self,login_password,options):
        self._login_password = login_password  
        self._sales = []
        self._driver = webdriver.Chrome(options)
        self._url = "https://fau.softcomshop.com.br/auth/login"

    def get_sales(self):
        return self._sales

    def try_run(self):
        self._try(self._run)

    def _run(self):        
        self._driver.get(self._url)
        self._try(self._logon,str(self._login_password[0]),str(self._login_password[1]))

        for indice in range(1,463):
            self._wait_find("""//*[@id="menu"]""")            
            self._driver.get(f"https://fau.softcomshop.com.br/nfe2/{indice}/editar")
            self._try(self._remov_pop_up)
            self._try(self._next_page)
            self._try(self._grup_sales)

            random_delay = np.random.uniform(1,3)
            time.sleep(random_delay)

        self._driver.quit()
    
    def _logon(self,login,senha):
        input_login = self._wait_find("""//*[@id="login-email"]""")
        input_senha = self._wait_find("""//*[@id="login-senha"]""")
        button_login = self._wait_find("""//*[@id="login-acessar"]""")        
        input_login.clear()
        input_login.send_keys(login)
        input_senha.clear()
        input_senha.send_keys(senha)
        button_login.click()
    
    def _get_range(self):
        indice = 1
        while True:
            url = f"https://fau.softcomshop.com.br/nfe2/{indice}"
            r = requests.get(url)
            if r.status_code == 404:
                return  indice
            elif r.status_code != 200:
                print(f"Atenção: status {r.status_code} na página {indice}, ignorando.")
                continue
            indice +1               
        
    def _grup_sales(self):        
        volumes = self._get_volumes()
               
        print(f"itens na nota: {volumes}")
        
        for indice in range(1,volumes+1):
            sold_book = self._try(self._get_products, indice)
            if sold_book is not None:
                self._sales.append(sold_book)

    def _get_volumes(self):
        str_volumes = self._wait_find("""/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div[2]/div[1]/div/div[2]/div/form/div[5]/div/div[1]/div[6]/span""").text
        int_volumes = int(float(str_volumes.replace(",",".")))
        return int_volumes
        
    def _get_products(self,indice):
        sold_book = {
                "CHAVE" : self._wait_find("""//*[@id="nfe-info"]/div[5]/span""").text,
                "NUMERO" : self._wait_find("""//*[@id="nfe-info"]/div[1]/span""").text,
                "CFOP": self._wait_find("""//*[@id="auto_natureza"]""").get_attribute("value"),
                "DATA" : self._wait_find("""//*[@id="data_hora_emissao"]""").get_attribute("value"),
                "ISBN" : self._wait_find(f"""/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div[1]/div[2]/div/table/tbody/tr[{indice}]/td[1]""").text,            
                "EXEMPLARES" : self._wait_find(f"""//*[@id="table-form-body"]/tr[{indice}]/td[4]""").text ,
                "VALOR_UNITARIO": self._wait_find(f"""//*[@id="table-form-body"]/tr[{indice}]/td[5]""").text,
                "VALOR_TOTAL": self._wait_find(f"""//*[@id="table-form-body"]/tr[{indice}]/td[6]""").text
                }              
        return sold_book

    def _remov_pop_up(self):           
            button_not_show =  WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".content-do-not-show-button")))
            button_not_show.click()

    def _next_page(self):
        
        next_btn = WebDriverWait(self._driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, """//*[@id="btn-next"]"""))
                )
        next_btn.click()
        print("next button ok")

    def _try(self,func,*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            with open("log.txt", "a", encoding="utf-8") as log:
                log.write(f"ERRO {func.__name__}: {str(e)}\n")
                print(f"Erro {func.__name__}")

    def _wait_find(self,element):
        return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
        