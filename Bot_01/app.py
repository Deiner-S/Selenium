from extraction_pages import ExtractionPages as ep
from selenium.webdriver.chrome.options import Options

import pandas as pd

op = Options()
op.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/115.0.0.0 Safari/537.36")

extract = ep(op)

extract.try_run()
dados =extract.data

# Transforma em DataFrame normal
#df = pd.DataFrame(dados)
#df.to_csv('saida.csv', index=False, encoding='utf-8-sig')