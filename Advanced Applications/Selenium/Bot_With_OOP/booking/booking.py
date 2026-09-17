from selenium import webdriver
from selenium.webdriver.edge.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from . import constants as const
import time
class Booking(webdriver.Edge):
    def __init__(self, teardown=False):
        self.teardown = teardown
        
        edge_options = Options()
        edge_options.add_experimental_option("detach", True) 
        
        super().__init__(options=edge_options)
        
        self.implicitly_wait(5)
        self.maximize_window()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self.teardown:
            self.quit()

    def wait(self,by,v):
        return WebDriverWait(self,10).until(
            EC.element_to_be_clickable((by , v))
        )

    def land_first_page(self):
        self.get(const.Base_URL)

    def change_currency(self,currency = 'USD'):

        close_ads = self.find_elements(*const.CLOSE_AD)
        if close_ads:
            close_ads[0].click()

        self.find_element(*const.CURRENCY_TRIGGER).click()
        self.wait(By.XPATH,f'//div[text()="{currency}"]/ancestor::button').click()
        
    def select_destination(self,destination = 'Alexandria'):

        search_feild = self.wait(*const.SEARCH_FEILD)
        search_feild.clear()
        search_feild.click()
        search_feild.send_keys(f"{destination}")

        time.sleep(1)
        selected = self.find_elements(*const.FIRST_RESULT_XPATH)
        selected[0].click()

        time.sleep(1)
    def select_date(self,go,back):
        self.wait(By.CSS_SELECTOR,f'span[data-date = "{go}"]').click()
        self.wait(By.CSS_SELECTOR,f'span[data-date = "{back}"]').click()

    def select_adult(self, target=10):

        self.find_element(*const.SEARCHADULT).click()
        time.sleep(1.5) 

        while True:
            try:
                display_element = self.wait(*const.ADULTS_COUNT_DISPLAY)
                current_text = self.execute_script(
                    "return arguments[0].innerText || arguments[0].textContent || arguments[0].innerHTML;", 
                    display_element
                )

                if not current_text or not current_text.strip().isdigit():
                    print("Waiting for number to appear...")
                    time.sleep(0.5)
                    continue
                # current_text = display_element.text -> Anthoer Solution
                current_num = int(current_text.strip())

                if current_num < target:
                    self.wait(*const.ADULTS_PLUS).click()
                    time.sleep(0.4) 
                elif current_num > target:
                    self.wait(*const.ADULTS_MINUS).click()
                    time.sleep(0.4)
                else:
                    print(f"🎯 Target {target} reached successfully!")
                    break
                    
            except Exception as e:
                print(f"Error occurred: {e}. Retrying...")
                time.sleep(1)
        self.find_element(*const.DONE_BUTTON).click() 
        self.wait(*const.SEARCH_BUTTON).click()       
    









