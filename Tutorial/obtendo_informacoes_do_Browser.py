from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev")

title = driver.title
url = driver.current_url

driver.quit()