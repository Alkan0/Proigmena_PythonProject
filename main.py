from selenium.webdriver.common.by import By
import pandas as pd
from selenium import webdriver

class Cryptos:
    def __init__(self, name, price, change24h, high420, low24, volumeCoin, volumeDollar):
        self.name = name
        self.price = price
        self.change24h = change24h
        self.high420 = high420
        self.low24 = low24
        self.volumeCoin = volumeCoin
        self.volumeDollar = volumeDollar

matrix = []

driver = webdriver.Chrome()
url = "https://www.binance.com/en/markets"
driver.get(url)
urll = driver.find_elements(By.CLASS_NAME, "css-1wp9rgv")
driver2 = webdriver.Chrome()
datas = '//div[contains(@class, "tickerPriceText")]'
driver.minimize_window()
driver2.minimize_window()

for x in range(10):
    url2 = "https://www.binance.com/el/trade/" + urll[x].text + "_BUSD"
    driver2.get(url2)
    name = driver2.find_elements(By.XPATH, "//*[starts-with(@style,'font-size: 20px; font-weight: 500;')]")
    price = driver2.find_elements(By.CLASS_NAME, "subPrice")
    values = driver2.find_elements(By.XPATH, datas)


    if (price.__len__() == 0):
        url2 = "https://www.binance.com/el/trade/" + urll[x].text + "BIDR"
        driver2.get(url2)
        price = driver2.find_elements(By.CLASS_NAME, "subPrice")
        name = driver2.find_elements(By.XPATH, "//*[starts-with(@style,'font-size: 20px; font-weight: 500;')]")
        values = driver2.find_elements(By.XPATH, datas)

    if (price.__len__() == 0):
        url2 = "https://www.binance.com/el/trade/" + urll[x].text + "_BIDR"
        driver2.get(url2)
        price = driver2.find_elements(By.CLASS_NAME, "subPrice")
        name = driver2.find_elements(By.XPATH, "//*[starts-with(@style,'font-size: 20px; font-weight: 500;')]")
        values = driver2.find_elements(By.XPATH, datas)


    if (price.__len__() == 0):
        url2 = "https://www.binance.com/el/trade/" + urll[x].text + "_BTC"
        driver2.get(url2)
        price = driver2.find_elements(By.CLASS_NAME, "subPrice")
        name = driver2.find_elements(By.XPATH, "//*[starts-with(@style,'font-size: 20px; font-weight: 500;')]")
        values = driver2.find_elements(By.XPATH, datas)
    matrix.append(Cryptos(name[0] ,price[0], values[0], values[1], values[2], values[3], values[4]))
    print(matrix[x].name.text)
    print(matrix[x].price.text)
    print(matrix[x].high420.text)
    print(matrix[x].low24.text)
    print(matrix[x].change24h.text)
    print(matrix[x].volumeCoin.text)
    print(matrix[x].volumeDollar.text)
    print("\n")


driver2.close()
driver.close()

df = pd.read_excel(r'Cryptos.xlsx')
print(df)


