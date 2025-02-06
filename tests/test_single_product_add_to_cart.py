import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.Products import ProductOverviewPage
from pageObjects.SearchResults import SearchResult
from pageObjects.addToCart import addToCart
from utilities.logging import Logger


@pytest.mark.usefixtures("setup")
class TestAdd_Single_Product_to_Cart(Logger):

    def test_search_box_present(self):
        log = self.get_logger()
        hp = HomePage(self.driver)
        assert hp.is_search_box_present(), "Search box is not found on the Home page"
        log.info("Search box is present on Home Page")  # Log success

    def test_homepage(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        search_term = self.test_home_data["search_term"]
        log.info(f"Searching for term: {search_term}")
        homePage.search_box().send_keys(search_term)  # Searching the product in Amazon & Submitting it
        homePage.submit()

    def test_search_results(self):
        log = self.get_logger()
        target_product_title = self.test_home_data["target_product_title"]
        search_results = SearchResult(self.driver)

        desired_product_found = search_results.find_desired_product(target_product_title)
        product_found = desired_product_found[0]
        element_index = desired_product_found[1]

        assert product_found.text is not None, "Product couldn't be found"
        log.info(f"Found product: {product_found.text}")  # Log found product

        search_results.navigate_to_product_overview(element_index)    # Navigating to Product Overview Pages

    def test_product_overview(self):
        target_product_title = self.test_home_data["target_product_title"]
        product_page = ProductOverviewPage(self.driver)

        product_page_title = product_page.product_title()
        assert all(part.lower() in product_page_title.lower() for part in target_product_title.split()), "Product Title isn't matching the Searched product"

        product_page.product_price()    # Checking the product price is present or not
        product_page.product_ratings()  # Checking the product ratings is present or not
        product_page.product_images()   # Getting the number of images in the product page

    def test_add_to_cart(self):
        log = self.get_logger()
        cartPage = addToCart(self.driver)  # Adding to the Cart
        log.info("Adding product to cart")  # Log adding to cart
        cartPage.add_to_cart_button()

        locator = "//span[@id='attach-accessory-cart-subtotal']"  # Waiting for the price to show up
        cartPage.verify_elements_visibility(locator)
        price_cart = cartPage.price_added_cart()  # Verifying the prices
        assert price_cart, "Failed to retrieve price after adding to cart"

        cartPage.cart_page()

    def test_add_quantity_cart(self):
        log = self.get_logger()
        modifyCart = addToCart(self.driver)
        modifyCart.modify_cart_add()

        log.info("Verifying the cart total")
        modifyCart.verify_cart_modification()

    def test_reduce_cart_quantity(self):
        log = self.get_logger()
        modifyCart = addToCart(self.driver)
        modifyCart.modify_cart_reduce()

    def test_delete_cart_quantity(self):
        log = self.get_logger()
        time.sleep(2)
        modifyCart = addToCart(self.driver)
        log.info("Deleting the product items from the cart")
        cart_removed_text = modifyCart.delete_cart()

        assert "removed" in cart_removed_text, "Product couldn't be deleted from the cart"