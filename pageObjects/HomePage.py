from selenium.webdriver.common.by import By
from utilities.logging import Logger


class HomePage(Logger):

    def __init__(self, driver):
        self.driver = driver

    search = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    submitButton = (By.XPATH, "//input[@id='nav-search-submit-button']")

    def is_search_box_present(self):
        try:
            # Attempt to locate the search box element
            self.driver.find_element(*HomePage.search)
            return True  # Search box is found
        except:
            return False  # Search box is not found

    def search_box(self):
        return self.driver.find_element(*HomePage.search)

    def submit(self):
        self.driver.find_element(*HomePage.submitButton).click()

    def to_cart_home_page(self):
        log = self.get_logger()
        go_to_cart_from_home = self.driver.find_element(By.XPATH, "//a[@id='nav-cart']")
        log.info("Navigating to Cart Page from HomePage")
        go_to_cart_from_home.click()