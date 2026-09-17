from selenium.webdriver.common.by import By

Base_URL = "https://www.booking.com"
CLOSE_AD = (By.CSS_SELECTOR, 'button[aria-label="Dismiss sign in information."]')
CURRENCY_TRIGGER = (By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
SEARCH_FEILD =  (By.NAME,'ss')
FIRST_RESULT_XPATH = (By.XPATH, '//li[@data-testid="autocomplete-result"] | //div[@data-testid="autocomplete-results-options"]//li[1]')
SEARCHADULT = (By.CSS_SELECTOR,'button[data-testid="occupancy-config"]')
ADULTS_INPUT = (By.ID, 'group_adults')
ADULTS_MINUS = (By.XPATH, "//label[@for='group_adults']/parent::div/following-sibling::div//button[1]")
ADULTS_PLUS = (By.XPATH, "//label[@for='group_adults']/parent::div/following-sibling::div//button[2]")
ADULTS_COUNT_DISPLAY = (By.XPATH, "//input[@id='group_adults']/preceding-sibling::span | //div[input[@id='group_adults']]//span[contains(@class, 'e32aa465fd')]")
DONE_BUTTON = (By.XPATH, "//button[contains(., 'Done')]")
# DONE_BUTTON = (By.XPATH, "//div[@id='occupancy-config']//button[last()]")
SEARCH_BUTTON = (By.CSS_SELECTOR,"button[type='submit']")

