from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)

    # =====================================
    # WAIT UNTIL ELEMENT CLICKABLE
    # =====================================

    def wait_until_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(locator))

    # =====================================
    # WAIT UNTIL ELEMENT VISIBLE
    # =====================================

    def wait_until_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver,
            timeout).until(EC.visibility_of_element_located(locator))

    # =====================================
    # CHECK DISPLAYED
    # =====================================

    def is_displayed(self, locator, timeout=20):

        try:
            element = self.wait_until_visible(locator,timeout)
            return element.is_displayed()

        except Exception:
            return False

    # =====================================
    # SCROLL INTO VIEW
    # =====================================

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",element)

    # =====================================
    # NORMAL CLICK
    # =====================================

    def click(self, locator):
        element = self.wait_until_clickable(locator)
        element.click()

    # =====================================
    # JS CLICK
    # =====================================

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();",element)

    # =====================================
    # SEND KEYS
    # =====================================

    def enter_text(self, locator, text):
        element = self.wait_until_visible(locator)
        element.clear()
        element.send_keys(text)

    # =====================================
    # SCROLL BY
    # =====================================

    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollBy({x}, {y});")

    # =====================================
    # HOVER
    # =====================================

    def hover_to_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    # =====================================
    # SWITCH TO NEW TAB
    # =====================================

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    # =====================================
    # GET CURRENT URL
    # =====================================

    def get_current_url(self):
        return self.driver.current_url