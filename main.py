import webbrowser


from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.binance.com/en/markets')

texts = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='tabContainer']//div[@direction='ltr']//div[@data-area='left']//div[@data-bn-type='text']")))]
coins = [texts[i] for i in range(len(texts)) if i % 3 == 1]
prices = [texts[i] for i in range(len(texts)) if i % 3 == 2]

print (coins)
print (prices)
driver.close()
