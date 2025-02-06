import pytest

from pageObjects.HomePage import HomePage
from pageObjects.Products import ProductOverviewPage
from pageObjects.SearchResults import SearchResult
from pageObjects.addToCart import addToCart
from utilities.logging import Logger


@pytest.mark.usefixtures("setup2")
class TestAdd_Multiple_Products_to_Cart(Logger):
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
            homePage.search_box().send_keys(search_term)
            homePage.submit()
            desired_product_found = search_results.find_desired_product(target_product_title)

            if desired_product_found:
                product_found = desired_product_found[0]
                element_index = desired_product_found[1]

                assert product_found.text is not None, f"Product {search_term} couldn't be found"
                log.info(f"Found product: {product_found.text}")

                search_results.navigate_to_product_overview(element_index)

                product_page_title = product_page.product_title()
                assert all(part.lower() in product_page_title.lower() for part in
                           target_product_title.split()), f"Product Title for {search_term} isn't matching"

                log.info("Adding product to cart")
                cartPage.add_to_cart_button()

                locator = "//span[@id='attach-accessory-cart-subtotal']"  # Waiting for the price to show up
                cartPage.verify_elements_visibility(locator)
                price_cart = cartPage.price_added_cart()  # Verifying the prices
                assert price_cart, "Failed to retrieve price after adding to cart"

            else:  # Handle the case where the product isn't found
                log.info(f"Desired product {search_term} not found. Skipping to next product.")
                continue  # Continue to the next iteration of the loop

            for window_handle in self.driver.window_handles:
                if window_handle != original_window:  # Find the new window
                    self.driver.switch_to.window(window_handle)
                    break  # Exit the loop once the new window is found

            self.driver.close()
            # Switch back to the original window
            self.driver.switch_to.window(original_window)

            homePage.search_box().clear()  # Correct way to call clear()

        log.info("Finished adding all products. Performing final cart verification (if needed).")
        homePage.to_cart_home_page()
        cartPage.verify_cart_modification()