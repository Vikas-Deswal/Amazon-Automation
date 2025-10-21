import pytest
import allure
from allure_commons.types import AttachmentType

from pageObjects.HomePage import HomePage
from pageObjects.Products import ProductOverviewPage
from pageObjects.SearchResults import SearchResult
from pageObjects.addToCart import addToCart
from utilities.logging import Logger


@pytest.mark.usefixtures("setup2")
@allure.epic("Amazon e-Commerce Flow")
@allure.feature("Add Multiple Products to Cart")
class TestAdd_Multiple_Products_to_Cart(Logger):
    @allure.story("Bulk Add To Cart Flow")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Add multiple products to cart and validate totals")
    @allure.description("Search multiple products sequentially, validate details, add each to cart, then verify cart summary.")
    def test_add_multiple_to_cart(self ):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        search_results = SearchResult(self.driver)
        product_page = ProductOverviewPage(self.driver)
        cartPage = addToCart(self.driver)

        original_window = self.driver.current_window_handle

        for product_data in self.test_multiple_data:
            search_term = product_data["search_term"]
            target_product_title = product_data["target_product_title"]

            log.info(f"Searching for product: {search_term}")
            allure.attach(str(search_term), name="search_term", attachment_type=AttachmentType.TEXT)
            allure.attach(str(target_product_title), name="target_product_title", attachment_type=AttachmentType.TEXT)
            with allure.step("Enter search term in the search box"):
                homePage.search_box().send_keys(search_term)
            with allure.step("Submit the search"):
                homePage.submit()
            with allure.step("Find the desired product in the search results"):
                desired_product_found = search_results.find_desired_product(target_product_title)

            if desired_product_found:
                product_found = desired_product_found[0]
                element_index = desired_product_found[1]

                with allure.step("Validate that a product element was found"):
                    assert product_found.text is not None, f"Product {search_term} couldn't be found"
                log.info(f"Found product: {product_found.text}")
                allure.attach(product_found.text, name="found_product_title", attachment_type=AttachmentType.TEXT)

                with allure.step("Navigate to Product Overview page"):
                    search_results.navigate_to_product_overview(element_index)

                with allure.step("Validate product title matches the target title"):
                    product_page_title = product_page.product_title()
                    allure.attach(product_page_title, name="product_overview_title", attachment_type=AttachmentType.TEXT)
                    assert all(part.lower() in product_page_title.lower() for part in
                               target_product_title.split()), f"Product Title for {search_term} isn't matching"

                log.info("Adding product to cart")
                with allure.step("Click 'Add to Cart' button"):
                    cartPage.add_to_cart_button()

                with allure.step("Capture and validate cart price"):
                    price_cart = cartPage.price_added_cart()  # Verifying the prices
                    allure.attach(str(price_cart), name="cart_price", attachment_type=AttachmentType.TEXT)
                    assert price_cart, "Failed to retrieve price after adding to cart"

            else:  # Handle the case where the product isn't found
                with allure.step("Desired product not found — skip to next"):
                    log.info(f"Desired product {search_term} not found. Skipping to next product.")
                continue  # Continue to the next iteration of the loop

            with allure.step("Switch to the newly opened window"):
                for window_handle in self.driver.window_handles:
                    if window_handle != original_window:  # Find the new window
                        self.driver.switch_to.window(window_handle)
                        break  # Exit the loop once the new window is found

            with allure.step("Close current product window and return to original"):
                self.driver.close()
                # Switch back to the original window
                self.driver.switch_to.window(original_window)

            with allure.step("Clear the search box for next product"):
                homePage.search_box().clear()  # Correct way to call clear()

        log.info("Finished adding all products. Performing final cart verification (if needed).")
        with allure.step("Navigate to cart from home page"):
            homePage.to_cart_home_page()
        with allure.step("Verify cart totals/modification after multiple additions"):
            cartPage.verify_cart_modification()