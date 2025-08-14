from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np

class ExtractBooksMetadata():
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._url = "https://www.buscaisbn.com.br"
        self._df = pd.read_csv("Book(CSV-ISBN-EDUFU).csv")
        self.table_data = []
    
    
    def run(self):
        self._try(self._extract_metadata,"FALHA AO TENTAR extrair")
        self._driver.quit()
    
    def macke_df(self):
        df_table_data = pd.DataFrame(self.table_data)
        df_table_data.to_csv("books_metadata.csv")
    
    def _search(self,isbn):
        input_text_box = self._wait_find("""//*[@id="search"]""")
        input_text_box.clear() 
        input_text_box.send_keys(isbn)
        submit_button = self._wait_find("/html/body/main/div[1]/div/div/div[2]/button")
        submit_button.click()


    def _extract_metadata(self):
        for isbn in self._df["ISBN"]:
            delay = np.random.uniform(1,2)
            self._try(self._search(isbn),"Falaha ao procurar dados")
            data = {"TITLE":self._wait_find("""//*[@id="result"]/div/div[2]/div/h4""").text,
                    "AUTHOR":self._wait_find("""//*[@id="result"]/div/div[2]/div/div/p""").text,
                    "ISBN":self._wait_find("""//*[@id="result"]/div/div[2]/div/p""").text,
                    "THEME1":self._wait_find("""//*[@id="result"]/div/div[3]/span[1]""").text,
                    "THEME2":self._wait_find("""//*[@id="result"]/div/div[3]/span[2]""").text,
                    "THEME3":self._wait_find("""//*[@id="result"]/div/div[3]/span[3]""").text,
                    "PUBLISHER":self._wait_find("""//*[@id="book_publisher"]""").text,
                    "BOOK_YEAR":self._wait_find("""//*[@id="book_year"]""").text,
                    "BOOK_PAGE_COUT":self._wait_find("""//*[@id="book_page_count"]""").text
            } 
                
            self.table_data.append(data)
                
            
            time.sleep(delay)
        


    
    def _wait_find(self,element):
        try: 
            return WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
        except Exception as e: 
            with open("log.txt", "a", encoding="utf-8") as log:
                log.write(f"{element} ERROR: {str(e)}\n")

    def _try(self,func,msg,*args,**kwargs):
        try:
            return func(*args,**kwargs)                            
        except Exception as e:
            with open("log.txt", "a", encoding="utf-8") as log:
                log.write(f"{msg} ERROR: {str(e)}\n")

if __name__ == "__main__":
    app = ExtractBooksMetadata()
    app.run()