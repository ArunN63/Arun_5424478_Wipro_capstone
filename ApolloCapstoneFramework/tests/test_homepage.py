from utils.driver_setup import get_driver

from pages.homepage import HomePage

import time


def test_homepage():

    driver = get_driver()
    homepage = HomePage(driver)
    assert homepage.is_homepage_loaded()
    print("Homepage loaded successfully")
    homepage.click_buy_medicines()
    homepage.switch_to_new_tab()
    print("Switched to Apollo Pharmacy tab")
    time.sleep(5)
    current_url = driver.current_url
    assert "apollo" in current_url
    print("Apollo Pharmacy page opened")
    driver.quit()