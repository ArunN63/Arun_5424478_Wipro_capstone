import time
import pytest

from utils.driver_setup import get_driver
from utils.logger import setup_logger

from pages.homepage import HomePage
from pages.health_condition_page import HealthConditionPage


logger = setup_logger()


class TestApolloPharmacy:

    @pytest.fixture
    def driver(self):
        driver = get_driver()
        yield driver
        driver.quit()
        logger.info("Browser closed")

    # ---------------------------
    # TC01
    # ADD PRODUCT + CART + MEMBERSHIP
    # ---------------------------

    def test_tc01_diabetes_care(self, driver):
        homepage = HomePage(driver)

        # HOMEPAGE ASSERT

        assert homepage.is_homepage_loaded()
        logger.info("Homepage loaded")

        # CLICK BUY MEDICINES

        homepage.click_buy_medicines()
        logger.info("Buy Medicines clicked")

        # HEALTH PAGE

        health_page = HealthConditionPage(driver)
        time.sleep(3)

        # SCROLL LITTLE

        health_page.scroll_down_little()
        logger.info("Scrolled little")

        # DIABETES CATEGORY

        health_page.click_health_condition_by_index(1)
        logger.info("Diabetes category opened")

        # PRODUCT PAGE ASSERT

        assert health_page.is_product_page_loaded()
        logger.info("Product page loaded")

        # WAIT PRODUCTS

        health_page.wait_for_products_to_load()
        logger.info("Products loaded")

        # ADD PRODUCT

        health_page.add_first_product_to_cart()
        logger.info("Product added")

        # OPEN CART

        health_page.open_cart()
        logger.info("Cart opened")

        # VERIFY CART PAGE

        current_url = driver.current_url
        print(f"Current URL: {current_url}")
        assert "medicines-cart" in current_url
        logger.info("Cart page verified")

        # ADD CIRCLE MEMBERSHIP

        health_page.add_circle_membership()
        logger.info("Circle Membership added")

        # SCREENSHOT

        driver.save_screenshot("screenshots/tc01_success.png")
        logger.info("Screenshot captured")

        # FINAL LOG

        logger.info("TC01 PASSED")

    # ---------------------------
    # TC02
    # ---------------------------

    def test_tc02_change_page_and_add_product(self, driver):
        homepage = HomePage(driver)
        assert homepage.is_homepage_loaded()
        homepage.click_buy_medicines()
        health_page = HealthConditionPage(driver)
        time.sleep(3)
        health_page.scroll_down_little()

        # LIVER CARE

        health_page.click_health_condition_by_index(4)
        assert health_page.is_product_page_loaded()

        # FILTERS

        health_page.apply_filters(max_filters=3)

        # PAGE 2

        moved = health_page.go_to_page(2)

        if not moved:
            health_page.go_to_next_page()

        # WAIT PRODUCTS

        health_page.wait_for_products_to_load()

        # ADD PRODUCT

        health_page.add_first_product_to_cart()
        driver.save_screenshot("screenshots/tc02_success.png")
        logger.info("TC02 PASSED")

    # ---------------------------
    # TC03
    # ORAL CARE FILTERS + ADD PRODUCT
    # ---------------------------

    def test_tc03_oral_care_add_product(self, driver):
        homepage = HomePage(driver)
        assert homepage.is_homepage_loaded()
        homepage.click_buy_medicines()
        health_page = HealthConditionPage(driver)
        time.sleep(3)
        health_page.scroll_down_little()

        # ORAL CARE

        health_page.click_health_condition_by_index(3)
        assert health_page.is_product_page_loaded()

        # APPLY 4 FILTERS

        health_page.apply_filters(max_filters=4)

        # WAIT PRODUCTS

        health_page.wait_for_products_to_load()

        # ADD PRODUCT

        health_page.add_first_product_to_cart()
        driver.save_screenshot("screenshots/tc03_oralcare_success.png")
        logger.info("TC03 PASSED")

    # ---------------------------
    # TC04
    # UPDATE CART QUANTITY
    # ---------------------------

    def test_tc04_update_cart_quantity(self, driver):
        homepage = HomePage(driver)
        assert homepage.is_homepage_loaded()
        homepage.click_buy_medicines()
        health_page = HealthConditionPage(driver)
        time.sleep(3)
        health_page.scroll_down_little()

        # ORAL CARE

        health_page.click_health_condition_by_index(3)
        assert health_page.is_product_page_loaded()

        # ADD PRODUCT

        health_page.add_first_product_to_cart()

        # INCREASE QUANTITY

        health_page.increase_quantity()

        # DECREASE QUANTITY

        health_page.decrease_quantity()
        driver.save_screenshot("screenshots/tc04_success.png")
        logger.info("TC04 PASSED")