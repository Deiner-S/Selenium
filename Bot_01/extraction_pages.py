from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExtractionPages():
    def __init__(self):
        self.data = {}
        self.driver = webdriver.Chrome()
        self.url = "https://fau.softcomshop.com.br/auth/login"

    def run(self,login,senha):
        self.driver.get(self.url)
        self._login(self.driver,login,senha)


        self.driver.quit()
        
    def _login(self,driver,login,senha):

        input_login = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#login-email"))
                )
        input_senha = driver.find_element(By.CSS_SELECTOR, "#login-senha")
        button_login = driver.find_element(By.CSS_SELECTOR, "#login-acessar")
        input_login.clear()
        input_login.send_keys(login)
        input_senha.clear()
        input_senha.send_keys(senha)
        button_login.click()


    def _get_register(self,driver):
        
        self.dados | {
        "CHAVE" : driver.find_element(By.XPATH, """//*[@id="nfe-info"]/div[5]/span""").text,
        "NUMERO" : driver.find_element(By.XPATH, """//*[@id="nfe-info"]/div[1]/span""").text,
        "DATA" : driver.find_element(By.XPATH, """//*[@id="data_hora_emissao"]""").get_attribute("value"),
        "CPF" : driver.find_element(By.XPATH, """//*[@id="destinatario_cpf_cnpj"]""").get_attribute("value"),
        "CEP": driver.find_element(By.XPATH, """//*[@id="destinatario_cep"]""").get_attribute("value"),
        "VALOR": driver.find_element(By.XPATH, """//*[@id="total_produto_valor"]""").text,
        "CFOP": driver.find_element(By.XPATH, """//*[@id="auto_natureza"]""").get_attribute("value")}


    def _get_products(self,driver):
        livros = []
        num_xpath_tr = len(driver.find_element(By.XPATH,"""//*[@id="table-form-body"]/tr"""))
        for indice in range(1,num_xpath_tr,+1):
            livro = {
            "ISBN" : driver.find_element(By.XPATH, f"""//*[@id="table-form-body"]/tr[{indice}]/td[1]""").text,
            "EXEMPLARES" : driver.find_element(By.XPATH, f"""//*[@id="table-form-body"]/tr[{indice}]/td[4]""").text,
            "VALOR_UNITARIO": driver.find_element(By.XPATH, f"""//*[@id="table-form-body"]/tr[{indice}]/td[5]""").text,
            "VALOR_TOTAL": driver.find_element(By.XPATH, f"""//*[@id="table-form-body"]/tr[{indice}]/td[6]""").text
            }
            livros.append(livro)

        self.dados | {"Livros":livros}
        

    def _get_financial(self,driver):

        self.dados | {
        "FORMA_PAGAMENTO" : driver.find_element(By.XPATH, """//*[@id="table-form-body"]/tr/td[1]""").text,
        "DESCONTO" : driver.find_element(By.XPATH, """//*[@id="total_desconto_percentual"]""").get_attribute("value")
        }

    def _remov_pop_up(driver):
        try:
                button_not_show = driver.find_element(By.CSS_SELECTOR, ".content-do-not-show-button")
                button_not_show.click()
        except Exception as e:
            with open("log.txt", "a", encoding="utf-8") as log:
                log.writelines(f"Erro: {str(e)}")
            print ("Botão não encontrado")

    def _next_page(self,driver):

        next_btn = driver.find_element(By.XPATH, """//*[@id="btn-next"]""")
        next_btn.click()

        
        