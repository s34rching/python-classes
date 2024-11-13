import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

IG_EMAIL = os.environ.get("IG_EMAIL")
IG_PASSWORD = os.environ.get("IG_PASSWORD")
IG_SIMILAR_ACCOUNT = "memes.com"
IG_URL = "https://www.instagram.com"
IG_DIALOG_ACCOUNTS_COUNT = 5
WAIT_TIMEOUT = 5


class FollowerBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.actions = actions = ActionChains(self.driver)

    def login(self):
        self.driver.get(IG_URL)

        accept_cookies_button = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='dialog'] button:nth-of-type(1)"))
        )
        accept_cookies_button.click()

        email_input = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
        )
        email_input.send_keys(IG_EMAIL)

        password_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(IG_PASSWORD)

        self.actions.key_down(Keys.ENTER).perform()

    def find_followers(self):
        search_icon = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Search']"))
        )
        search_icon.click()

        search_input = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search input']"))
        )
        search_input.send_keys(IG_SIMILAR_ACCOUNT)

        target_account = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/memes/']"))
        )
        target_account.click()

        followers_counter_label = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/memes/followers/']"))
        )
        followers_counter_label.click()

    def follow(self):
        WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='dialog'] input[aria-label='Search input']"))
        )

        WebDriverWait(self.driver, WAIT_TIMEOUT).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, "div[role='dialog'] button")) > IG_DIALOG_ACCOUNTS_COUNT
        )

        dialog_buttons = self.driver.find_elements(By.CSS_SELECTOR, "div[role='dialog'] button")

        follow_buttons = dialog_buttons[1:]
        buttons_to_click = follow_buttons[0:5]

        for follow_button in buttons_to_click:
            time.sleep(2)
            follow_button.click()
