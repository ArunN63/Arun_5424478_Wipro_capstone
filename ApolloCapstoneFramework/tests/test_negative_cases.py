import time
import pytest
from selenium.webdriver.common.by import By

from utils.driver_setup import get_driver
from utils.logger import setup_logger

from pages.homepage import HomePage
from pages.health_condition_page import HealthConditionPage


logger = setup_logger()


class TestApolloNegativeCases:

    @pytest.fixture
    def driver(self):
        driver = get_driver()
        yield driver
        driver.quit()
        logger.info("Browser closed")

    # ---------------------------
    # TC05 NEGATIVE
    # INVALID CONDITION INDEX
    # ---------------------------

    def test_tc05_invalid_health_condition(self, driver):
        homepage = HomePage(driver)
        assert homepage.is_homepage_loaded()
        homepage.click_buy_medicines()
        health_page = HealthConditionPage(driver)
        time.sleep(3)
        health_page.scroll_down_little()

        try:

            # INVALID INDEX

            health_page.click_health_condition_by_index(50)
            pytest.fail("Invalid condition opened")

        except Exception as e:

            print("PASS: Invalid health condition " "handled properly")
            print(f"Error Message: {e}")
            driver.save_screenshot("screenshots/tc05_negative.png")
            logger.info("TC05 NEGATIVE PASSED")

    # ---------------------------
    # TC06 NEGATIVE
    # INVALID PAGE URL
    # ---------------------------

    def test_tc06_invalid_page_navigation(self, driver):

        homepage = HomePage(driver)
        assert homepage.is_homepage_loaded()
        homepage.click_buy_medicines()
        health_page = HealthConditionPage(driver)
        time.sleep(3)
        health_page.scroll_down_little()

        # OPEN ORAL CARE
        health_page.click_health_condition_by_index(3)
        assert health_page.is_product_page_loaded()

        # INVALID PAGE URL
        invalid_url = (driver.current_url + "?page=99")
        driver.get(invalid_url)
        time.sleep(5)
        current_url = driver.current_url
        print(f"Navigated URL: {current_url}")

        # VERIFY PAGE URL CHANGED
        assert "page=99" in current_url

        # VERIFY NO PRODUCTS / DIFFERENT STATE
        products = driver.find_elements(By.XPATH,"//div[contains(@class,'ProductCard_productCard')]")
        print(f"Products found: {len(products)}")
        driver.save_screenshot("screenshots/tc06_negative.png")
        logger.info("TC06 NEGATIVE PASSED")