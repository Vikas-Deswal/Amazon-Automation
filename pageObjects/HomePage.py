from selenium.common.exceptions import NoSuchElementException
from pageObjects.locators import HomePageLocators
from utilities.BasePage import BaseActions

class HomePage(BaseActions):

    def is_search_box_present(self):
        try:
            # Attempt to locate the search box element
            self.element_is_visible(HomePageLocators.search_box)
            self.driver.find_element(*HomePageLocators.search_box)
            return True  # Search box is found
        except NoSuchElementException:
            return False  # Search box is not found

    def search_box(self):
        self.element_is_visible(HomePageLocators.search_box)
        return self.driver.find_element(*HomePageLocators.search_box)

    def submit(self):
        self.element_is_visible(HomePageLocators.submit_button)
        self.driver.find_element(*HomePageLocators.submit_button).click()

    def to_cart_home_page(self):
        log = self.get_logger()
        self.element_is_visible(HomePageLocators.cart_icon)
        go_to_cart_from_home = self.driver.find_element(*HomePageLocators.cart_icon)
        log.info("Navigating to Cart Page from HomePage")
        go_to_cart_from_home.click()