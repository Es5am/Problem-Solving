import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_for(driver, by, value, timeout=50): 
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value))
    )


os.environ['PATH'] += r"D:\Work\Elzero\Python\Lib\Selenium"

driver = webdriver.Edge()

driver.get('https://www.saucedemo.com/')
time.sleep(2)

username = driver.find_element(By.ID,"user-name").send_keys("standard_user")
password = driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(2)


login = driver.find_element(By.ID,"login-button").click()
time.sleep(2)


print('-'*50) # Seprator

items = driver.find_elements(By.CLASS_NAME,"inventory_item") # Select The Container Of Products
print(f'The Number Of Products In Our Store is {len(items)} Product.') # Get The Number Of Products
print('This Is Our Products : ') 
count = 1

for item in items: # Loop On Products
    name  = item.find_element(By.CLASS_NAME,"inventory_item_name").text # Get Name Of Products
    price = item.find_element(By.CLASS_NAME,"inventory_item_price").text # Get Price Of Products
    print(f'{count}. {name} And It Costs {price}.')
    count += 1
    print('-'*50) # Seprator

nav_bar = wait_for(driver,By.ID,"react-burger-menu-btn")
nav_bar.click()
time.sleep(2)

logout = wait_for(driver,By.ID,"logout_sidebar_link")
logout.click()

input('Press Enter To Close ...')