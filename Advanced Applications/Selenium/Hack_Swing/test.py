import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait(b,v) :
    return WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((b,v))
    )

os.environ["PATH"] += r"D:\Work\Elzero\Python\Lib\Selenium" # Create Path
driver = webdriver.Edge()

driver.get("https://www.saucedemo.com/") # Get Targeted Website

driver.find_element(By.ID,"user-name").send_keys("standard_user") # Get And Fill User_Name
driver.find_element(By.ID,"password").send_keys("secret_sauce") # Get And Fill Password
driver.find_element(By.ID,"login-button").click() # Click Login Button

# time.sleep(2) # Stop For 2 Seconds 

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

wait(By.ID,'react-burger-menu-btn').click() # Click The Nav Bar
wait(By.ID,'logout_sidebar_link').click() # Click On Log Out 

input('Press Enter To Close ...')



