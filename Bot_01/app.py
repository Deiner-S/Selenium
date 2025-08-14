from sale_extractor import SaleExtractor as se
from selenium.webdriver.chrome.options import Options
import pandas as pd

class App():

    def __init__(self):
        self.options = Options()
        self.argument = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) ""AppleWebKit/537.36 (KHTML, like Gecko) ""Chrome/115.0.0.0 Safari/537.36"
    
    
    def run(self):        
        self.options.add_argument(self.argument)

        sales_extractor= se(self.options)
        sales_extractor.try_run()

        sales = sales_extractor.sales
        print(sales)
        # Transforma em DataFrame normal
        df = pd.DataFrame(sales)
        df.to_csv('sales.csv', index=False, encoding='utf-8-sig')


if __name__ == "__main__":
    app = App()
    app.run()
