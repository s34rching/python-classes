import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os

TWITTER_USERNAME = os.environ.get("TWITTER_NAME")
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
TWEET_PUBLISHED_TEXT = "Пост отправлен."
SPEEDTEST_URL = "https://www.speedtest.net"
MEASUREMENT_TIME_SEC = 50
X_LOGIN_URL = "https://x.com/i/flow/login"
TWITTER_ANIMATION_TIME_SECS = 5
WAIT_TIMEOUT_SEC = 10


class ComplainingBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 200
        self.down = 20

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)

        accept_data_privacy_button = WebDriverWait(self.driver, WAIT_TIMEOUT_SEC).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button#onetrust-accept-btn-handler"))
        )
        accept_data_privacy_button.click()

        go_button = WebDriverWait(self.driver, WAIT_TIMEOUT_SEC).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.start-text"))
        )
        go_button.click()

        time.sleep(MEASUREMENT_TIME_SEC)

        download_value_label = self.driver.find_element(By.CSS_SELECTOR, "span[data-download-status-value]")
        upload_value_label = self.driver.find_element(By.CSS_SELECTOR, "span[data-upload-status-value]")

        return {
            "download_value": float(download_value_label.text),
            "upload_value": float(upload_value_label.text)
        }

    def tweet_at_provider(self, speed_values):
        if speed_values["download_value"] < self.down or speed_values["upload_value"] < self.up:
            actions = ActionChains(self.driver)

            self.driver.get(X_LOGIN_URL)

            time.sleep(TWITTER_ANIMATION_TIME_SECS)

            username_input = WebDriverWait(self.driver, WAIT_TIMEOUT_SEC).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[autocomplete='username']"))
            )
            username_input.send_keys(TWITTER_EMAIL)
            actions.key_down(Keys.ENTER).perform()

            confirm_account_input = WebDriverWait(self.driver, WAIT_TIMEOUT_SEC).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='ocfEnterTextTextInput']"))
            )
            confirm_account_input.send_keys(TWITTER_USERNAME)
            actions.key_down(Keys.ENTER).perform()

            password_input = WebDriverWait(self.driver, WAIT_TIMEOUT_SEC).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
            )
            password_input.send_keys(TWITTER_PASSWORD)
            actions.key_down(Keys.ENTER).perform()

            new_tweet_container = WebDriverWait(self.driver, WAIT_TIMEOUT_SEC).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0RichTextInputContainer']"))
            )
            new_tweet_container.click()

            new_tweet_textarea = WebDriverWait(self.driver, WAIT_TIMEOUT_SEC).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']"))
            )
            new_tweet_textarea.send_keys(f"Hey P, why is my speed is"
                                         f" {speed_values["download_value"]}/{speed_values["upload_value"]}"
                                         f" when I pay for {self.down}/{self.up}"
                                         )
            actions.key_down(Keys.ENTER).perform()

            publish_button = WebDriverWait(self.driver, WAIT_TIMEOUT_SEC).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']"))
            )
            publish_button.click()

            post_published_toast = WebDriverWait(self.driver, WAIT_TIMEOUT_SEC).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='toast']"))
            )
            assert TWEET_PUBLISHED_TEXT in post_published_toast.text
