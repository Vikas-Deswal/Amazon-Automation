import time
import allure

from allure_commons.types import AttachmentType

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.Products import ProductOverviewPage
from pageObjects.SearchResults import SearchResult
from pageObjects.addToCart import addToCart
from utilities.logging import Logger


@pytest.mark.usefixtures("setup")
@allure.epic("Amazon e-Commerce Flow")
@allure.feature("Single product Search and Add to Cart")
class TestAdd_Single_Product_to_Cart(Logger):

    @allure.story("Home Page Validation")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Verify search box is present on Home Page")
    @allure.description("Ensure user can see the search box on Amazon home page before starting the flow.")
    def test_search_box_present(self):
        log = self.get_logger()
        hp = HomePage(self.driver)
        with allure.step("Check that search box is visible on the Home Page"):
            assert hp.is_search_box_present(), "Search box is not found on the Home page"
        log.info("Search box is present on Home Page")  # Log success
        allure.attach("Search box found on Home Page", name="ui-check", attachment_type=AttachmentType.TEXT)

    @allure.story("Product Search")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Search a product from Home Page")
    @allure.description("Enter search term and submit to navigate to search results.")
    def test_homepage(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        search_term = self.test_home_data["search_term"]
        allure.attach(str(search_term), name="search_term", attachment_type=AttachmentType.TEXT)
        log.info(f"Searching for term: {search_term}")
        with allure.step("Type the search term in the search box"):
            homePage.search_box().send_keys(search_term)  # Searching the product in Amazon & Submitting it
        with allure.step("Submit the search"):
            homePage.submit()

    @allure.story("Search Results Navigation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Locate the desired product in search results and open overview")
    @allure.description("Find target product in results and navigate to its overview page.")
    def test_search_results(self):
        log = self.get_logger()
        target_product_title = self.test_home_data["target_product_title"]
        search_results = SearchResult(self.driver)

        with allure.step("Find the desired product from search results"):
            desired_product_found = search_results.find_desired_product(target_product_title)
            product_found = desired_product_found[0]
            element_index = desired_product_found[1]

        with allure.step("Validate that the desired product is found"):
            assert product_found.text is not None, "Product couldn't be found"
        log.info(f"Found product: {product_found.text}")  # Log found product
        allure.attach(product_found.text, name="found_product_title", attachment_type=AttachmentType.TEXT)

        with allure.step("Navigate to the Product Overview page"):
            search_results.navigate_to_product_overview(element_index)    # Navigating to Product Overview Pages

    @allure.story("Product Overview Validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify product overview details")
    @allure.description("Validate title, price, ratings, and images are present on product overview page.")
    def test_product_overview(self):
        target_product_title = self.test_home_data["target_product_title"]
        product_page = ProductOverviewPage(self.driver)

        with allure.step("Read product title and validate it matches the searched term"):
            product_page_title = product_page.product_title()
            allure.attach(product_page_title, name="product_overview_title", attachment_type=AttachmentType.TEXT)
            assert all(part.lower() in product_page_title.lower() for part in target_product_title.split()), "Product Title isn't matching the Searched product"

        with allure.step("Verify product price is visible"):
            product_page.product_price()    # Checking the product price is present or not
        with allure.step("Verify product ratings are visible"):
            product_page.product_ratings()  # Checking the product ratings is present or not
        with allure.step("Count product images in the gallery"):
            product_page.product_images()   # Getting the number of images in the product page

    @allure.story("Add To Cart")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Add the product to cart and validate price")
    @allure.description("Add product to cart and verify that the cart price is captured.")
    def test_add_to_cart(self):
        log = self.get_logger()
        cartPage = addToCart(self.driver)  # Adding to the Cart
        log.info("Adding product to cart")  # Log adding to cart
        with allure.step("Click 'Add to Cart' button"):
            cartPage.add_to_cart_button()

        with allure.step("Capture the price from cart"):
            price_cart = cartPage.price_added_cart()  # Verifying the prices
            allure.attach(str(price_cart), name="cart_price", attachment_type=AttachmentType.TEXT)
        print(price_cart)
        with allure.step("Verify price is present after adding to cart"):
            assert price_cart, "Failed to retrieve price after adding to cart"

    @allure.story("Cart Modification")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Increase quantity in cart and verify total")
    @allure.description("Increase cart quantity and validate the cart totals are updated.")
    def test_add_quantity_cart(self):
        log = self.get_logger()
        modifyCart = addToCart(self.driver)
        with allure.step("Increase product quantity in cart"):
            modifyCart.modify_cart_add()

        log.info("Verifying the cart total")
        with allure.step("Verify cart totals reflect increased quantity"):
            modifyCart.verify_cart_modification()

    @allure.story("Cart Modification")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Reduce quantity in cart")
    @allure.description("Modify the cart quantity by one unit.")
    def test_reduce_cart_quantity(self):
        log = self.get_logger()
        time.sleep(2)
        modifyCart = addToCart(self.driver)
        with allure.step("Reduce product quantity in cart"):
            modifyCart.modify_cart_reduce()

    @allure.story("Cart Cleanup")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Remove product from cart")
    @allure.description("Delete product from cart and validate cart is cleared.")
    def test_delete_cart_quantity(self):
        log = self.get_logger()
        time.sleep(2)
        modifyCart = addToCart(self.driver)
        log.info("Deleting the product items from the cart")
        with allure.step("Delete the product from the cart"):
            cart_removed_text = modifyCart.delete_cart()

        with allure.step("Verify the product was removed from cart"):
            allure.attach(cart_removed_text, name="cart_status_text", attachment_type=AttachmentType.TEXT)
            assert "removed" in cart_removed_text, "Product couldn't be deleted from the cart"