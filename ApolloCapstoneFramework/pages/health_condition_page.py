from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.basepage import BasePage

import time


class HealthConditionPage(BasePage):

    PRODUCT_CONTAINER = (By.XPATH,"//div[contains(@class,'ProductCard_productCardGrid')]")

    FIRST_ADD_BUTTON = (By.XPATH,"(//button[contains(.,'Add')])[1]")

    CART_BUTTON = (By.XPATH,"//a[contains(@href,'medicines-cart')]")

    # ---------------------------
    # SCROLL
    # ---------------------------

    def scroll_down_little(self):
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)

    # ---------------------------
    # CLICK HEALTH CONDITION
    # ---------------------------

    def click_health_condition_by_index(self, index):
        condition = self.wait_until_clickable((By.XPATH,f"(//div[@id='Browse by Health Conditions Web']//a)[{index}]"),20)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",condition)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();",condition)
        print(f"Clicked condition {index}")
        time.sleep(1)

    # ---------------------------
    # PRODUCT PAGE CHECK
    # ---------------------------

    def is_product_page_loaded(self):

        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.PRODUCT_CONTAINER))
            print("Product page loaded")
            return True

        except Exception as e:
            print("Product page failed")
            print(e)
            return False

    # ---------------------------
    # WAIT PRODUCTS
    # ---------------------------

    def wait_for_products_to_load(self):

        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    self.PRODUCT_CONTAINER
                )
            )
            time.sleep(2)

        except Exception as e:
            print("Products load failed:",e)

    # ---------------------------
    # APPLY FILTERS
    # ---------------------------

    def apply_filters(self, max_filters=4):
        time.sleep(3)
        checkboxes = self.driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        print(f"Found {len(checkboxes)} checkboxes")
        count = 0

        for checkbox in checkboxes:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",checkbox)
                time.sleep(3)
                self.driver.execute_script("arguments[0].click();",checkbox)
                count += 1
                print(f"Applied filter {count}")
                time.sleep(3)
                if count == max_filters:
                    break

            except Exception as e:
                print("Checkbox failed")
                print(e)

        print(f"Successfully applied {count} filters")
        time.sleep(3)

    # ---------------------------
    # ADD PRODUCT
    # ---------------------------

    def add_first_product_to_cart(self):

        try:
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0, 400);")
            time.sleep(2)

            add_buttons = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_all_elements_located(
                    (
                        By.XPATH,
                        "//button[contains(.,'Add')]"
                    )
                )
            )
            print(f"Found {len(add_buttons)} add buttons")
            first_button = add_buttons[0]
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",first_button)
            time.sleep(1)

            self.driver.execute_script("arguments[0].click();",first_button)
            print("Added product to cart")
            time.sleep(1)

        except Exception as e:
            print(f"Add to cart failed: {e}")
            raise

    # ---------------------------
    # PAGINATION
    # ---------------------------

    def go_to_page(self, page_number):

        try:
            page = WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,f"//*[@id='product-container']/div[2]/ul/li[{page_number}]/a")))
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",page)
            time.sleep(2)

            self.driver.execute_script("arguments[0].click();",page)
            print(f"Moved to page {page_number}")
            time.sleep(2)
            return True

        except Exception as e:

            print(f"Page {page_number} navigation failed:",e)
            return False

    # ---------------------------
    # NEXT PAGE
    # ---------------------------

    def go_to_next_page(self):

        try:

            next_btn = WebDriverWait(
                self.driver,
                15
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//*[@id='product-container']/div[2]/ul/a[2]/li"
                    )
                )
            )

            self.driver.execute_script("arguments[0].click();",next_btn)
            print("Moved to next page")
            time.sleep(2)
            return True

        except Exception as e:
            print("Next page failed:",e)
            return False

    # ---------------------------
    # INCREASE QUANTITY
    # ---------------------------

    def increase_quantity(self):

        try:

            time.sleep(3)

            plus_btn = WebDriverWait(
                self.driver,
                20
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//span[@role='button' and @aria-label='Increase button']"
                    )
                )
            )

            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",plus_btn)

            time.sleep(1)

            self.driver.execute_script(
                "arguments[0].click();",
                plus_btn
            )

            print("Quantity increased")
            time.sleep(3)

        except Exception as e:

            print("Increase quantity failed:",e)
            raise

    # ---------------------------
    # DECREASE QUANTITY
    # ---------------------------

    def decrease_quantity(self):

        try:

            time.sleep(3)

            minus_btn = WebDriverWait(
                self.driver,
                20
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//span[@role='button' and @aria-label='Decrease button']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                minus_btn
            )

            time.sleep(1)

            self.driver.execute_script(
                "arguments[0].click();",
                minus_btn
            )

            print("Quantity decreased")
            time.sleep(3)

        except Exception as e:
            print("Decrease quantity failed:",e)
            raise

    # ---------------------------
    # INVALID SEARCH
    # ---------------------------

    def search_invalid_product(self, text):

        try:

            time.sleep(3)

            search_box = WebDriverWait(
                self.driver,
                20
            ).until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        "input[type='search']"
                    )
                )
            )

            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",search_box)
            time.sleep(1)
            search_box.click()
            time.sleep(1)
            search_box.clear()
            search_box.send_keys(text)

            print(f"Searched invalid product: {text}")
            time.sleep(2)
            search_box.send_keys(Keys.ENTER)
            print("Search submitted")
            time.sleep(5)

        except Exception as e:
            print("Search failed:",e)
            raise

    # ---------------------------
    # OPEN CART
    # ---------------------------

    def open_cart(self):

        cart_btn = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.element_to_be_clickable(
                self.CART_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            cart_btn
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            cart_btn
        )

        WebDriverWait(
            self.driver,
            20
        ).until(
            lambda d: "cart" in d.current_url.lower()
        )

        print("Cart opened")

        time.sleep(5)

    # ---------------------------
    # ENTER MOBILE NUMBER
    # ---------------------------

    def enter_mobile_number(self, mobile):

        try:

            print("Waiting for mobile input...")

            mobile_input = WebDriverWait(
                self.driver,
                40
            ).until(
                EC.visibility_of_element_located(
                    (
                        By.NAME,
                        "mobileNumber"
                    )
                )
            )

            mobile_input.click()

            time.sleep(2)

            mobile_input.clear()

            mobile_input.send_keys(mobile)

            print("Mobile number entered")

            time.sleep(5)

        except Exception as e:

            print(
                "Mobile input failed:",
                e
            )

            raise

    # ---------------------------
    # CLICK CONTINUE
    # LOGIN ARROW BUTTON
    # ---------------------------

    def click_continue(self):

        try:

            print("Waiting for login arrow button...")

            time.sleep(5)

            continue_btn = WebDriverWait(
                self.driver,
                40
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[@title='Login'] | //button[contains(@class,'newLogin_btn')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                continue_btn
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                continue_btn
            )

            print("Arrow login button clicked")

            time.sleep(8)

        except Exception as e:

            print(
                "Continue failed:",
                e
            )

            raise

    # ---------------------------
    # CLICK PROCEED
    # CART PAGE BUTTON
    # ---------------------------

    def click_proceed(self):

        try:

            proceed_btn = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[contains(.,'Proceed')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                proceed_btn
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                proceed_btn
            )

            print("Proceed clicked")

            time.sleep(5)

        except Exception as e:

            print(
                "Proceed failed:",
                e
            )

            raise

    # ---------------------------
    # CHECK LOGIN POPUP
    # ---------------------------

    def is_login_popup_present(self):

        try:

            WebDriverWait(
                self.driver,
                5
            ).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//input[@type='tel']"
                    )
                )
            )

            print("Login popup present")

            return True

        except Exception:

            print("Login popup not present")

            return False

    # ---------------------------
    # CLICK ADD ADDRESS
    # ---------------------------

    def click_add_address(self):

        add_address = WebDriverWait(
            self.driver,
            30
        ).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(.,'ADD ADDRESS')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            add_address
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            add_address
        )

        print("ADD ADDRESS clicked")

        time.sleep(5)

    # ---------------------------
    # CLICK TEXT SAFELY
    # ---------------------------

    def click_text_element_safely(self, text_value, timeout=12):

        print(
            f"Trying to click: {text_value}"
        )

        end_time = time.time() + timeout

        while time.time() < end_time:

            clicked = self.driver.execute_script(
                """
                const target = arguments[0].toLowerCase();

                const elements = Array.from(
                    document.querySelectorAll(
                        'button, a, div, span, p'
                    )
                );

                function isVisible(el) {

                    const style =
                        window.getComputedStyle(el);

                    const rect =
                        el.getBoundingClientRect();

                    return (
                        style.display !== 'none' &&
                        style.visibility !== 'hidden' &&
                        rect.width > 0 &&
                        rect.height > 0
                    );
                }

                for (const el of elements) {

                    if (!isVisible(el)) {
                        continue;
                    }

                    const text = (
                        el.innerText ||
                        el.textContent ||
                        ''
                    ).trim().toLowerCase();

                    if (
                        text === target ||
                        text.includes(target)
                    ) {

                        el.scrollIntoView({
                            block: 'center'
                        });

                        el.click();

                        return true;
                    }
                }

                return false;
                """,
                text_value
            )

            if clicked:

                print(
                    f"Clicked: {text_value}"
                )

                time.sleep(3)

                return True

            time.sleep(1)

        raise Exception(
            f"Could not click: {text_value}"
        )



    # ---------------------------
    # CLICK SELECT ADDRESS
    # ---------------------------

    def click_select_address(self):

        try:

            print(
                "Waiting for SELECT ADDRESS..."
            )

            select_btn = WebDriverWait(
                self.driver,
                40
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//*[contains(text(),'SELECT ADDRESS')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                select_btn
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                select_btn
            )

            print(
                "SELECT ADDRESS clicked"
            )

            time.sleep(4)

        except Exception as e:

            print(
                "SELECT ADDRESS failed:",
                e
            )

            raise


    # ---------------------------
    # CLICK ADD NEW ADDRESS
    # ---------------------------

    def click_add_new_address(self):

        try:

            print(
                "Waiting for Add New Address..."
            )

            add_new_btn = WebDriverWait(
                self.driver,
                40
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//*[contains(text(),'Add New Address')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                add_new_btn
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                add_new_btn
            )

            print(
                "Add New Address clicked"
            )

            time.sleep(8)

        except Exception as e:

            print(
                "Add New Address failed:",
                e
            )

            raise

    # ---------------------------
    # SELECT LOCATION
    # ---------------------------

    def select_location(self, location):

        try:

            print(
                "Waiting for search input..."
            )

            search_box = WebDriverWait(
                self.driver,
                40
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "input[placeholder*='Search for society']"
                    )
                )
            )

            search_box.clear()

            search_box.send_keys(
                location
            )

            print(
                f"{location} entered"
            )

            time.sleep(1)

            # GET ALL SEARCH RESULTS

            results = WebDriverWait(
                self.driver,
                40
            ).until(
                EC.presence_of_all_elements_located(
                    (
                        By.XPATH,
                        "//div[contains(@class,'NewSearchLocationSuggestor_searchItemList')]"
                    )
                )
            )

            print(
                f"Found {len(results)} location results"
            )

            clicked = False

            for result in results:

                text = result.text.strip()

                print(
                    "Result found:",
                    text
                )

                # SKIP SAVED ADDRESS

                if (
                        location.lower() in text.lower()
                        and "Home" not in text
                ):
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block:'center'});",
                        result
                    )

                    time.sleep(2)

                    self.driver.execute_script(
                        "arguments[0].click();",
                        result
                    )

                    print(
                        f"{location} search result selected"
                    )

                    clicked = True

                    break

            if not clicked:
                raise Exception(
                    f"{location} search result not found"
                )

            time.sleep(3)

        except Exception as e:

            print(
                f"{location} selection failed:",
                e
            )

            raise

    # ---------------------------
    # ENTER ADDRESS DETAILS
    # ---------------------------

    def enter_address_details(self):

        try:

            print(
                "Entering address details..."
            )

            # HOUSE / FLAT FIELD

            house_input = WebDriverWait(
                self.driver,
                40
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "textarea[name='address1']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                house_input
            )

            time.sleep(2)

            house_input.clear()

            house_input.send_keys(
                "4-234"
            )

            print(
                "House number entered"
            )

            time.sleep(3)

            # SCROLL DOWN TO BUTTON

            self.driver.execute_script(
                "window.scrollBy(0, 700);"
            )

            time.sleep(3)

            # SAVE & NEXT BUTTON

            save_next_btn = WebDriverWait(
                self.driver,
                40
            ).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//button[contains(.,'Save & Next')]"
                    )
                )
            )

            print(
                "Save button found"
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                save_next_btn
            )

            time.sleep(3)

            self.driver.execute_script(
                "arguments[0].click();",
                save_next_btn
            )

            print(
                "Save & Next clicked"
            )

            time.sleep(1)

        except Exception as e:

            print(
                "Address details failed:",
                e
            )

            raise

    # ---------------------------
    # ENTER RECIPIENT DETAILS
    # ---------------------------

    def enter_recipient_details(self):

        try:

            print(
                "Entering recipient details..."
            )

            time.sleep(1)

            # SCROLL LITTLE DOWN

            self.driver.execute_script(
                "window.scrollBy(0, 300);"
            )

            time.sleep(2)

            # SELECT OFFICE BUTTON

            office_btn = WebDriverWait(
                self.driver,
                40
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[@id='OFFICE']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                office_btn
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                office_btn
            )

            print(
                "Office selected"
            )

            time.sleep(3)

            # RECIPIENT NAME FIELD

            recipient_input = WebDriverWait(
                self.driver,
                40
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//input[@name='recipientName']"
                    )
                )
            )

            recipient_input.clear()

            recipient_input.send_keys(
                "Pavan"
            )

            print(
                "Recipient name entered"
            )

            time.sleep(3)

            # SCROLL FULL DOWN

            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            time.sleep(5)

            # SAVE ADDRESS BUTTON

            save_btn = WebDriverWait(
                self.driver,
                60
            ).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//button[contains(., 'Save Address')]"
                    )
                )
            )

            # SCROLL BUTTON INTO VIEW

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                save_btn
            )

            time.sleep(3)

            # FORCE BUTTON VISIBLE

            self.driver.execute_script(
                """
                arguments[0].style.display='block';
                arguments[0].style.visibility='visible';
                """,
                save_btn
            )

            time.sleep(2)

            # FORCE CLICK USING JS

            self.driver.execute_script(
                "arguments[0].click();",
                save_btn
            )

            print(
                "Save Address clicked"
            )

            time.sleep(10)

        except Exception as e:

            print(
                "Recipient details failed:",
                e
            )

            raise
    # ---------------------------
    # SEARCH LOCATION
    # ---------------------------

    def search_location(self, location):

        search_box = WebDriverWait(
            self.driver,
            30
        ).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//input[contains(@placeholder,'Search')]"
                )
            )
        )

        search_box.click()

        time.sleep(2)

        search_box.send_keys(location)

        print("Location entered")

        time.sleep(2)

        first_option = WebDriverWait(
            self.driver,
            30
        ).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//*[contains(text(),'{location}')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            first_option
        )

        print("Location selected")

        time.sleep(2)

    # ---------------------------
    # ADD CIRCLE MEMBERSHIP
    # ---------------------------

    def add_circle_membership(self):

        try:
            print("Checking cart items...")

            # VERIFY CART ITEMS PRESENT

            cart_items = WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located((By.XPATH,"//*[contains(text(),'ITEMS IN YOUR CART')]")))
            assert len(cart_items) > 0
            print("Cart items present")
            time.sleep(1)

            # SCROLL LITTLE UP

            self.driver.execute_script("window.scrollBy(0, -400);")
            time.sleep(1)

            print("Searching Circle Membership...")

            # FIND MEMBERSHIP BUTTON

            membership_buttons = self.driver.find_elements(By.XPATH,"//p[contains(text(), 'Save 15% on Medicines & get Free Lab test worth ₹500')]/ancestor::div[contains(@class, 'cardMain')]//button[contains(@class, 'ctaBtn')]")

            # IF MEMBERSHIP AVAILABLE

            if len(membership_buttons) > 0:
                add_btn = membership_buttons[0]
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",add_btn)
                time.sleep(1)

                self.driver.execute_script("arguments[0].click();",add_btn)
                print("Circle Membership added")
                time.sleep(1)

            else:
                print("Circle Membership not available")

        except Exception as e:
            print("Membership section skipped:",e)