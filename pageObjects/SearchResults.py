from pageObjects.locators import SearchResultLocators
from selenium.webdriver import ActionChains
from utilities.BasePage import BaseActions

class SearchResult(BaseActions):

    def find_desired_product(self, desired_product):
        log = self.get_logger()
        self.element_clickable(SearchResultLocators.items_list)
        search_list = self.driver.find_elements(*SearchResultLocators.items_list)
        for index, search_item in enumerate(search_list):
            try:
                name_element = search_item.find_element(*SearchResultLocators.item_name)
                name = name_element.text
                desired_product_parts = desired_product.lower().split()
                # Check if all key parts are present in the product name
                if all(part in name.lower() for part in desired_product_parts):
                    log.info(f"Desired product found at index: {index}")
                    return [search_item, index]
            except Exception as e:
                log.error(f"Error in finding the desired product: {e}")

    def navigate_to_product_overview(self,index):
        action = ActionChains(self.driver)
        product_to_click = self.driver.find_elements(*SearchResultLocators.link_to_overview)
        action.move_to_element(product_to_click[index]).click().perform()
        windOpened = self.driver.window_handles
        self.driver.switch_to.window(windOpened[1])
