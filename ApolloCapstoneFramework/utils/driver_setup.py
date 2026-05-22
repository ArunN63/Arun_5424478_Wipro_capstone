from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import config


def get_driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-notifications")

    options.add_experimental_option(
        "detach",
        False
    )

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    driver.maximize_window()

    driver.implicitly_wait(
        config.IMPLICIT_WAIT
    )

    driver.set_page_load_timeout(30)

    driver.get(
        config.BASE_URL
    )

    return driver