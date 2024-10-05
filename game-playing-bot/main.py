from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import time

BASE_URL = "https://orteil.dashnet.org/experiments/cookie/"
CLICK_TIMEOUT = 0.2


def is_upgrade_active(button_element):
    return button_element.get_attribute("class") != "grayed"


driver = webdriver.Chrome()
driver.get(BASE_URL)

game_end = datetime.now() + timedelta(minutes=10)
check_time = datetime.now() + timedelta(seconds=5)

while datetime.now() < game_end:
    time.sleep(CLICK_TIMEOUT)

    cookie_button = driver.find_element(By.ID, "cookie")
    cookie_button.click()

    if datetime.now() > check_time:
        byu_cursor_button = driver.find_element(By.ID, "buyCursor")
        byu_grandma_button = driver.find_element(By.ID, "buyGrandma")
        byu_factory_button = driver.find_element(By.ID, "buyFactory")
        byu_mine_button = driver.find_element(By.ID, "buyMine")
        byu_shipment_button = driver.find_element(By.ID, "buyShipment")
        byu_alchemy_lab_button = driver.find_element(By.ID, "buyAlchemy lab")
        byu_portal_button = driver.find_element(By.ID, "buyPortal")
        byu_time_machine_button = driver.find_element(By.ID, "buyTime machine")
        byu_elder_pledge_button = driver.find_element(By.ID, "buyElder Pledge")

        buttons = [
            byu_elder_pledge_button,
            byu_time_machine_button,
            byu_portal_button,
            byu_alchemy_lab_button,
            byu_shipment_button,
            byu_mine_button,
            byu_factory_button,
            byu_grandma_button,
            byu_cursor_button,
        ]

        for button in buttons:
            if is_upgrade_active(button):
                button.click()

        check_time += timedelta(seconds=5)

performance_label = driver.find_element(By.ID, "cps")
print(performance_label.text)
