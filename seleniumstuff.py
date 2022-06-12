from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://moscowteslaclub.ru/cars/"
driver.get(url)
cars = driver.find_elements(By.CSS_SELECTOR,
                            "article.car-available")
data = []
for car in cars:
    carname = car.find_element(By.CSS_SELECTOR, "h2.title").get_attribute("innerHTML")
    car_price1 = car.find_element(By.CSS_SELECTOR, "table.price")
    price1 = car_price1.find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
    car_featutes = car.find_element(By.CSS_SELECTOR, "div.main-props")
    racing = car_featutes.find_elements(By.CSS_SELECTOR, "td.value")[0].get_attribute("innerHTML")
    maxspeed = car_featutes.find_elements(By.CSS_SELECTOR, "td.value")[1].get_attribute("innerHTML")
    reserve = car_featutes.find_elements(By.CSS_SELECTOR, "td.value")[2].get_attribute("innerHTML")
    data.append([carname, price1, racing, maxspeed, reserve])

df1 = pd.DataFrame(data, columns=['Model', 'Price', 'Speed up time', 'Max speed', 'Power reserve'])

url2 = "https://moscowteslaclub.ru/cars/?PAGEN_1=2"
driver.get(url2)
cars2 = driver.find_elements(By.CSS_SELECTOR,
                             "article.car-available")
data2 = []
for car in cars2:
    carname = car.find_element(By.CSS_SELECTOR, "h2.title").get_attribute("innerHTML")
    car_price1 = car.find_element(By.CSS_SELECTOR, "table.price")
    price1 = car_price1.find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
    car_featutes = car.find_element(By.CSS_SELECTOR, "div.main-props")
    racing = car_featutes.find_elements(By.CSS_SELECTOR, "td.value")[0].get_attribute("innerHTML")
    maxspeed = car_featutes.find_elements(By.CSS_SELECTOR, "td.value")[1].get_attribute("innerHTML")
    reserve = car_featutes.find_elements(By.CSS_SELECTOR, "td.value")[2].get_attribute("innerHTML")
    data2.append([carname, price1, racing, maxspeed, reserve])
df2 = pd.DataFrame(data2, columns=['Model', 'Price', 'Speed up time', 'Max speed', 'Power reserve'])
url3 = "https://moscowteslaclub.ru/cars/?PAGEN_1=3"
driver.get(url3)
cars3 = driver.find_elements(By.CSS_SELECTOR,
                             "article.car-available")
data3 = []
for car in cars3:
    carname = car.find_element(By.CSS_SELECTOR, "h2.title").get_attribute("innerHTML")
    car_price1 = car.find_element(By.CSS_SELECTOR, "table.price")
    price1 = car_price1.find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
    car_featutes = car.find_element(By.CSS_SELECTOR, "div.main-props")
    racing = car_featutes.find_elements(By.CSS_SELECTOR, "td.value")[0].get_attribute("innerHTML")
    maxspeed = car_featutes.find_elements(By.CSS_SELECTOR, "td.value")[1].get_attribute("innerHTML")
    reserve = car_featutes.find_elements(By.CSS_SELECTOR, "td.value")[2].get_attribute("innerHTML")
    data3.append([carname, price1, racing, maxspeed, reserve])
df3 = pd.DataFrame(data3, columns=['Model', 'Price', 'Speed up time', 'Max speed', 'Power reserve'])
url4 = "https://moscowteslaclub.ru/cars/?PAGEN_1=4"
driver.get(url4)
cars4 = driver.find_elements(By.CSS_SELECTOR,
                             "article.car-available")
data4 = []
for car in cars4:
    carname = car.find_element(By.CSS_SELECTOR, "h2.title").get_attribute("innerHTML")
    car_price1 = car.find_element(By.CSS_SELECTOR, "table.price")
    price1 = car_price1.find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
    car_featutes = car.find_element(By.CSS_SELECTOR, "div.main-props")
    racing = car_featutes.find_elements(By.CSS_SELECTOR, "td.value")[0].get_attribute("innerHTML")
    maxspeed = car_featutes.find_elements(By.CSS_SELECTOR, "td.value")[1].get_attribute("innerHTML")
    reserve = car_featutes.find_elements(By.CSS_SELECTOR, "td.value")[2].get_attribute("innerHTML")
    data4.append([carname, price1, racing, maxspeed, reserve])
df4 = pd.DataFrame(data4, columns=['Model', 'Price', 'Speed up time', 'Max speed', 'Power reserve'])
final_data = df1.append([df2, df3, df4], ignore_index=True)
final_data = final_data.sort_values('Model')
final_data = final_data.reset_index().drop('index', axis=1)[17:40]
final_data = final_data.reset_index().drop('index', axis=1)