from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import time


class SaleExtractor():
    def __init__(self,login,senha,options):
        self._login = login
        self._senha = senha
        self.sales = []
        self._driver = webdriver.Chrome(options)
        self._url = "https://fau.softcomshop.com.br/auth/login"
        

    def try_run(self):
        self._try(self._run)

    def _run(self):        
        self._driver.get(self._url)
        self._try(self._logon,self._login,self._senha)

        for indice in range(423,425):
            self._wait_find("""//*[@id="menu"]""")            
            self._driver.get(f"https://fau.softcomshop.com.br/nfe2/{indice}/editar")            
            self._try(self._extract)
            
            random_delay = np.random.uniform(1,3)
            time.sleep(random_delay)

        self._driver.quit()

    def _extract(self):
        self._try(self._remov_pop_up) 
        self._next_page()
        self._grup_sales()        
        
    def _logon(self,login,senha):
        input_login = self._wait_find("""//*[@id="login-email"]""")
        input_senha = self._wait_find("""//*[@id="login-senha"]""")
        button_login = self._wait_find("""//*[@id="login-acessar"]""")        
        input_login.clear()
        input_login.send_keys(login)
        input_senha.clear()
        input_senha.send_keys(senha)
        button_login.click()


    
        
        data = {
        "CHAVE" : self._driver.find_element(By.XPATH, """//*[@id="nfe-info"]/div[5]/span""").text,
        "NUMERO" : self._driver.find_element(By.XPATH, """//*[@id="nfe-info"]/div[1]/span""").text,
        "DATA" : self._driver.find_element(By.XPATH, """//*[@id="data_hora_emissao"]""").get_attribute("value"),
        #"CPF" : self._driver.find_element(By.XPATH, """//*[@id="destinatario_cpf_cnpj"]""").get_attribute("value"),
        #"CEP": self._driver.find_element(By.XPATH, """//*[@id="destinatario_cep"]""").get_attribute("value"),
        #"VALOR": self._driver.find_element(By.XPATH, """/html/body/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div[2]/div[3]/div[2]/form/div/div[7]/div/div/div[2]/div/form/div[5]/div/div[1]/div[8]/span""").text,
        "CFOP": self._driver.find_element(By.XPATH, """//*[@id="auto_natureza"]""").get_attribute("value")}
        print("get register ok")
        return data

    def _grup_sales(self):        
        self._wait_find("""//*[@id="nfe-items"]""")
        num_xpath_tr = len(self._driver.find_elements(By.XPATH,"""//*[@id="table-form-body"]/tr"""))
        print(f"itens na nota: {num_xpath_tr}")
        
        for indice in range(1,num_xpath_tr):
            sold_book = self._try(self._get_products, indice)
            if sold_book is not None:
                self.sales.append(sold_book)            
        return 
        
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
        
        