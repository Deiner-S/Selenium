from selenium.webdriver.common.by import By
class ExtractionPages():
    def __init__(self):
        self.data = {}

    def register(self,driver):

        
        self.dados | {
        "CHAVE" : driver.find_element(By.XPATH, """//*[@id="nfe-info"]/div[5]/span""").text,
        "NUMERO" : driver.find_element(By.XPATH, """//*[@id="nfe-info"]/div[1]/span""").text,
        "DATA" : driver.find_element(By.XPATH, """//*[@id="data_hora_emissao"]""").get_attribute("value"),
        "CPF" : driver.find_element(By.XPATH, """//*[@id="destinatario_cpf_cnpj"]""").get_attribute("value"),
        "CEP": driver.find_element(By.XPATH, """//*[@id="destinatario_cep"]""").get_attribute("value"),
        "VALOR": driver.find_element(By.XPATH, """//*[@id="total_produto_valor"]""").text,
        "CFOP": driver.find_element(By.XPATH, """//*[@id="auto_natureza"]""").get_attribute("value")}


    def products(self,driver):
        self.dados | {
        "CHAVE" : driver.find_element(By.XPATH, """//*[@id="nfe-info"]/div[5]/span""").text,
        "NUMERO" : driver.find_element(By.XPATH, """//*[@id="nfe-info"]/div[1]/span""").text,
        "DATA" : driver.find_element(By.XPATH, """//*[@id="data_hora_emissao"]""").get_attribute("value"),
        "CPF" : driver.find_element(By.XPATH, """//*[@id="destinatario_cpf_cnpj"]""").get_attribute("value"),
        "CEP": driver.find_element(By.XPATH, """//*[@id="destinatario_cep"]""").get_attribute("value"),
        "VALOR": driver.find_element(By.XPATH, """//*[@id="total_produto_valor"]""").text,
        "CFOP": driver.find_element(By.XPATH, """//*[@id="auto_natureza"]""").get_attribute("value")}

    def financial(self,driver):

        self.dados | {
        "CHAVE" : driver.find_element(By.XPATH, """//*[@id="nfe-info"]/div[5]/span""").text,
        "NUMERO" : driver.find_element(By.XPATH, """//*[@id="nfe-info"]/div[1]/span""").text,
        "DATA" : driver.find_element(By.XPATH, """//*[@id="data_hora_emissao"]""").get_attribute("value"),
        "CPF" : driver.find_element(By.XPATH, """//*[@id="destinatario_cpf_cnpj"]""").get_attribute("value"),
        "CEP": driver.find_element(By.XPATH, """//*[@id="destinatario_cep"]""").get_attribute("value"),
        "VALOR": driver.find_element(By.XPATH, """//*[@id="total_produto_valor"]""").text,
        "CFOP": driver.find_element(By.XPATH, """//*[@id="auto_natureza"]""").get_attribute("value")}

    def removpopup(driver):
        try:
                button_not_show = driver.find_element(By.CSS_SELECTOR, ".content-do-not-show-button")
                button_not_show.click()
        except Exception as e:
            with open("log.txt", "a", encoding="utf-8") as log:
                log.writelines(f"Erro: {str(e)}")
            print ("Botão não encontrado")