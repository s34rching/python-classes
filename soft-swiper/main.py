from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

BASE_URL = "https://tinder.com/"
DASHBOARD = f"{BASE_URL}/app/recs"
ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")
ELEMENT_AWAIT_TIMEOUT = 10
SEARCH_MATCHES_WAIT = 45
INTRO_ANIMATION_TIMEOUT = 10
HUMANIZED_WAIT = 10
REJECT_COUNT = 5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
actions = ActionChains(driver)

driver.get(DASHBOARD)

time.sleep(3)

log_in_button = WebDriverWait(driver, ELEMENT_AWAIT_TIMEOUT).until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Log in"))
)

log_in_button.click()

log_in_modal = WebDriverWait(driver, ELEMENT_AWAIT_TIMEOUT).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-labelledby="MODAL_LOGIN"]'))
)

driver.switch_to.frame(log_in_modal.find_element(By.CSS_SELECTOR, 'iframe:nth-of-type(1)'))
sign_in_with_google_button = driver.find_element(By.CSS_SELECTOR, 'div[role="button"]')
sign_in_with_google_button.click()

WebDriverWait(driver, ELEMENT_AWAIT_TIMEOUT).until(
    EC.number_of_windows_to_be(2)
)

driver.switch_to.window(driver.window_handles[1])

email_input = WebDriverWait(driver, ELEMENT_AWAIT_TIMEOUT).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
)
email_input.send_keys(ACCOUNT_EMAIL)
submit_email_button = driver.find_element(By.CSS_SELECTOR, 'div[data-primary-action-label="Next"] button:nth-of-type(1)')
submit_email_button.click()

password_input = WebDriverWait(driver, ELEMENT_AWAIT_TIMEOUT).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
)
password_input.send_keys(ACCOUNT_PASSWORD)
submit_password_button = driver.find_element(By.CSS_SELECTOR, 'div[data-primary-action-label="Next"] button:nth-of-type(1)')
submit_password_button.click()

driver.switch_to.window(driver.window_handles[0])

grant_location_permission_button = WebDriverWait(driver, ELEMENT_AWAIT_TIMEOUT).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-modal="true"] button[aria-label="Allow"]'))
)
grant_location_permission_button.click()

grant_notifications_permission_button = WebDriverWait(driver, ELEMENT_AWAIT_TIMEOUT).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-modal="true"] button[aria-label="Notify me"]'))
)
grant_notifications_permission_button.click()

accept_privacy_settings = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Privacy preferences"] button:nth-of-type(1)')
accept_privacy_settings.click()

person_card = WebDriverWait(driver, SEARCH_MATCHES_WAIT).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Card stack"]'))
)

reject_button = WebDriverWait(driver, INTRO_ANIMATION_TIMEOUT).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.gamepad-icon-wrapper'))
)

for _ in range(0, REJECT_COUNT):
    actions.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()
    time.sleep(HUMANIZED_WAIT)
