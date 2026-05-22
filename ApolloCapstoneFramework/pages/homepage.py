from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.basepage import BasePage

import time


class HomePage(BasePage):

    BUY_MEDICINES_BUTTON = (By.XPATH,"(//a[contains(text(),'Buy Medicines')])[1]")

    HOME_LOGO = (By.XPATH,"//img[contains(@src,'apollo247.svg')]")

    POPUP_CLOSE_BUTTON = (By.XPATH,"//button//*[name()='svg']")

    # ---------------------------
    # CLOSE POPUP
    # ---------------------------

    def close_popup_if_present(self):

        try:

            popup = self.wait_until_clickable(self.POPUP_CLOSE_BUTTON,5)

            self.scroll_into_view(popup)
            self.js_click(popup)

            print("Popup closed")
            time.sleep(2)

        except Exception:
            print("No popup found")

    # ---------------------------
    # CLICK BUY MEDICINES
    # ---------------------------

    def click_buy_medicines(self):

        self.close_popup_if_present()
        medicine_btn = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.BUY_MEDICINES_BUTTON))

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",medicine_btn)
        ActionChains(self.driver).move_to_element(medicine_btn).perform()
        time.sleep(2)

        print("Button text:",medicine_btn.text)
        print("Button href:",medicine_btn.get_attribute("href"))
        self.driver.execute_script("arguments[0].click();",medicine_btn)
        print("Clicked Buy Medicines")
        time.sleep(5)

    # ---------------------------
    # SWITCH TAB
    # ---------------------------

    def switch_to_new_tab(self):
        time.sleep(3)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        print("Switched to new tab")
        time.sleep(5)

    # ---------------------------
    # HOMEPAGE CHECK
    # ---------------------------

    def is_homepage_loaded(self):
        return self.is_displayed(self.HOME_LOGO,20)

    # ---------------------------
    # GO TO HOMEPAGE
    # ---------------------------

    def go_to_apollo_homepage(self):
        self.driver.get("https://www.apollopharmacy.in/")
        print("Navigated back to Apollo homepage")
        time.sleep(5)