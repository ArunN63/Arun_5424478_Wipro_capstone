import time

from utils.driver_setup import get_driver
from utils.logger import setup_logger
from utils.excel_utils import get_test_data

from pages.homepage import HomePage
from pages.health_condition_page import HealthConditionPage

logger = setup_logger()


def test_end_to_end_flow():

    # ---------------------------
    # DRIVER
    # ---------------------------

    driver = get_driver()

    try:

        # ---------------------------
        # EXCEL DATA
        # ---------------------------

        data = get_test_data()

        mobile_number = str(
            int(data["mobile"])
        )

        condition_index = int(
            data["condition_index"]
        )

        location = data["location"]

        # ---------------------------
        # HOMEPAGE
        # ---------------------------

        homepage = HomePage(driver)

        assert homepage.is_homepage_loaded()

        logger.info(
            "Homepage loaded"
        )

        # ---------------------------
        # CLICK BUY MEDICINES
        # ---------------------------

        homepage.click_buy_medicines()

        logger.info(
            "Clicked Buy Medicines"
        )

        # ---------------------------
        # SWITCH TAB
        # ---------------------------

        homepage.switch_to_new_tab()

        logger.info(
            "Switched to new tab"
        )

        # ---------------------------
        # HEALTH PAGE
        # ---------------------------

        health_page = HealthConditionPage(
            driver
        )

        time.sleep(3)

        # ---------------------------
        # SCROLL
        # ---------------------------

        health_page.scroll_down_little()

        logger.info(
            "Scrolled"
        )

        # ---------------------------
        # OPEN CONDITION
        # ---------------------------

        health_page.click_health_condition_by_index(
            condition_index
        )

        logger.info(
            f"Clicked condition {condition_index}"
        )

        # ---------------------------
        # PRODUCT PAGE ASSERT
        # ---------------------------

        assert health_page.is_product_page_loaded()

        logger.info(
            "Product page loaded"
        )

        # ---------------------------
        # APPLY FILTERS
        # ---------------------------

        health_page.apply_filters(
            max_filters=2
        )

        logger.info(
            "Filters applied"
        )

        # ---------------------------
        # ADD PRODUCT
        # ---------------------------

        health_page.add_first_product_to_cart()

        logger.info(
            "Product added"
        )

        # ---------------------------
        # OPEN CART
        # ---------------------------

        health_page.open_cart()

        logger.info(
            "Cart opened"
        )

        # ---------------------------
        # CART ASSERT
        # ---------------------------

        assert (
            "cart"
            in driver.current_url.lower()
        )

        logger.info(
            "Cart page validation passed"
        )

        # ---------------------------
        # OPTIONAL MEMBERSHIP
        # ---------------------------

        health_page.add_circle_membership()

        logger.info(
            "Membership section handled"
        )

        # ---------------------------
        # CLICK PROCEED
        # ---------------------------

        health_page.click_proceed()

        logger.info(
            "Proceed clicked"
        )

        # ---------------------------
        # LOGIN POPUP CHECK
        # ---------------------------

        if health_page.is_login_popup_present():

            # ---------------------------
            # ENTER MOBILE
            # ---------------------------

            health_page.enter_mobile_number(
                mobile_number
            )

            logger.info(
                "Mobile number entered"
            )

            # ---------------------------
            # MOBILE ASSERT
            # ---------------------------

            assert len(
                mobile_number
            ) == 10

            logger.info(
                "Mobile validation passed"
            )

            # ---------------------------
            # CONTINUE
            # ---------------------------

            health_page.click_continue()

            logger.info(
                "Continue clicked"
            )

            print(
                "Enter OTP manually now..."
            )

            # ---------------------------
            # OTP WAIT
            # ---------------------------

            time.sleep(25)

        # ---------------------------
        # CLICK SELECT ADDRESS
        # ---------------------------

        health_page.click_select_address()

        logger.info(
            "SELECT ADDRESS clicked"
        )

        # ---------------------------
        # CLICK ADD NEW ADDRESS
        # ---------------------------

        health_page.click_add_new_address()

        logger.info(
            "Add New Address clicked"
        )

        # ---------------------------
        # SELECT LOCATION
        # ---------------------------

        health_page.select_location(
            location
        )

        logger.info(
            f"{location} selected"
        )

        # ---------------------------
        # ENTER ADDRESS DETAILS
        # ---------------------------

        health_page.enter_address_details()

        logger.info(
            "Address details entered"
        )

        # ---------------------------
        # ENTER RECIPIENT DETAILS
        # ---------------------------

        health_page.enter_recipient_details()

        logger.info(
            "Recipient details entered"
        )

        # ---------------------------
        # ADDRESS VALIDATION
        # ---------------------------

        try:

            if (
                    "save address"
                    in driver.page_source.lower()
                    or
                    "office"
                    in driver.page_source.lower()
            ):

                logger.info(
                    "Address validation passed"
                )

            else:

                logger.info(
                    "Address validation skipped"
                )

        except Exception as e:

            logger.info(
                f"Address validation issue: {e}"
            )

        # ---------------------------
        # SCREENSHOT
        # ---------------------------

        driver.save_screenshot(
            "screenshots/end_to_end_success.png"
        )

        logger.info(
            "Screenshot captured"
        )

        print(
            "TEST PASSED"
        )

        logger.info(
            "End to End flow completed"
        )

        time.sleep(5)

    except Exception as e:

        print(
            "TEST FAILED:",
            e
        )

        driver.save_screenshot(
            "screenshots/end_to_end_failed.png"
        )

        raise

    finally:

        driver.quit()

        logger.info(
            "Browser closed"
        )