from sale_extractor import SaleExtractor as se
from selenium.webdriver.chrome.options import Options
from cryptography.fernet import Fernet
import pandas as pd

class App():

    def __init__(self):
        self._options = Options()
        self._chave = b'9xxYPUDp8ZK1R67zIEwnozyTktVfpF6Cr5C4kbbmZPM='  
        self._fernet = Fernet(self._chave)
    
    def run(self):        
        self._configure_options()

        sales_extractor= se(self._options,423,427)
        sales_extractor.try_run()
        sales = sales_extractor.get_sales()
        print(sales)
        # Transforma em DataFrame normal

        df = pd.DataFrame(sales)
        df.to_csv('sales.csv', index=False, encoding='utf-8-sig')

    def _decrypt_login(self):
        with open('encrypt_login.txt', 'rb') as arquivo:
            dados_criptografados = arquivo.read()    
            dados_descriptografados = self._fernet.decrypt(dados_criptografados)
            login_senha = dados_descriptografados.decode().split("\n")
            return login_senha
        
    def _configure_options(self):
        self._options.add_argument("--headless")
        self._options.add_argument("--disable-gpu")
        self._options.add_argument("--window-size=1920,1080")
        self._options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) ""AppleWebKit/537.36 (KHTML, like Gecko) ""Chrome/115.0.0.0 Safari/537.36")
if __name__ == "__main__":
    app = App()
    app.run()
