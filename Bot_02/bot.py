from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np

driver = webdriver.Chrome()
driver.get("https://www.buscaisbn.com.br")
df = pd.read_csv("C:/Users/deiner.souza/Documents/Selenium/Bot_02/Book(CSV-ISBN-EDUFU).csv")
isbn_list = df["ISBN"]
delay = np.random.uniform(1,2)
table_data = []

for isbn in isbn_list:
    try:
        input_text_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        input_text_box.clear()  # Limpa o campo antes de digitar
        input_text_box.send_keys(isbn)

        submit_button = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div[2]/button")
        submit_button.click()

        # Espera até que o resultado do ISBN seja carregado
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, """//*[@id="result"]/div/div[2]"""))
        )

        data = {"TITLE":driver.find_element(By.XPATH, """//*[@id="result"]/div/div[2]/div/h4""").text,
                "AUTHOR":driver.find_element(By.XPATH,"""//*[@id="result"]/div/div[2]/div/div/p""").text,
                "ISBN":driver.find_element(By.XPATH, """//*[@id="result"]/div/div[2]/div/p""").text,
                "THEME1":driver.find_element(By.XPATH, """//*[@id="result"]/div/div[3]/span[1]""").text,
                "THEME2":driver.find_element(By.XPATH, """//*[@id="result"]/div/div[3]/span[2]""").text,
                "THEME3":driver.find_element(By.XPATH, """//*[@id="result"]/div/div[3]/span[3]""").text,
                "PUBLISHER":driver.find_element(By.XPATH, """//*[@id="book_publisher"]""").text,
                "BOOK_YEAR":driver.find_element(By.XPATH, """//*[@id="book_year"]""").text,
                "BOOK_PAGE_COUT":driver.find_element(By.XPATH, """//*[@id="book_page_count"]""").text
        } 
        
        table_data.append(data)
        
    except Exception as e:
        with open("log.txt", "a", encoding="utf-8") as log:
            log.write(f"EXTRACT {isbn} ERROR: {str(e)}\n")
    time.sleep(delay)

df_table_data = pd.DataFrame(table_data)
df_table_data.to_csv("books_metadata.csv")


driver.quit()
