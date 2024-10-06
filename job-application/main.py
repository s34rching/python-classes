from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import os
import time

BASE_URL = "https://www.linkedin.com"
SIGN_IN_URL = f"{BASE_URL}/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
FILTERED_JOBS_URL = f"{BASE_URL}/jobs/collections/easy-apply/?currentJobId=4029230519&discover=recommended&discoveryOrigin=JOBS_HOME_JYMBII"
ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")
WAIT_TIMEOUT = 10
JOBS_PER_PAGE = 25


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
actions = ActionChains(driver)
driver.get(SIGN_IN_URL)

# Sign In page
email_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
submit_login_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Sign in']")

email_input.send_keys(ACCOUNT_EMAIL)
password_input.send_keys(ACCOUNT_PASSWORD)
submit_login_button.click()

# Dashboard page
EC.visibility_of_element_located((By.CSS_SELECTOR, "span[title='Jobs']"))
driver.get(FILTERED_JOBS_URL)

# Jobs list page
jobs_container = WebDriverWait(driver, WAIT_TIMEOUT).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.scaffold-layout__list-container"))
)

for job_index in range(1, JOBS_PER_PAGE + 1):
    time.sleep(1)

    job_card = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f"li[data-occludable-job-id]:nth-of-type({job_index})"))
    )

    actions.move_to_element(job_card).perform()
    job_card.click()

    position_title = job_card.find_element(By.TAG_NAME, "strong").text

    WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f"div[aria-label='{position_title}']"))
    )

    save_job_button = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button.jobs-save-button"))
    )

    save_job_button.click()
