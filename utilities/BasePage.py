# utilities/BaseActions.py
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.logging import Logger
import re

class BaseActions(Logger):
    def __init__(self, driver):
        self.driver = driver
    
    def element_is_visible(self, locator):
        element_to_show = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (locator)))
        return element_to_show

    def element_clickable(self, locator):
        element_to_show = WebDriverWait(self.driver, 6).until(
            expected_conditions.element_to_be_clickable(
                (locator)))
        return element_to_show
    
    def extract_price(self, output):
        """
        Extracts the price from the given output string.

        Args:
        output: The input string containing the price.

        Returns:
        The extracted price as an integer, or None if no price is found.
        """
        # Remove currency symbol and commas
        price_str = output.replace("₹", "").replace(",", "")

        # Extract the price using regular expression
        match = re.search(r"(\d+\.\d+)", price_str)

        if match:
            price_float = float(match.group(1))
            return price_float
        else:
            return None
