from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.logging import Logger
from utilities.PriceOperations import PriceOperations


class addToCart(Logger):
    def __init__(self, driver):
        self.driver = driver

    cart = (By.XPATH, "(//input[@id='add-to-cart-button'])[2]")
    alternative_locator = (By.XPATH, "//input[@id='add-to-cart-button']")
    priceAdded = (By.XPATH, "//span[@id='attach-accessory-cart-subtotal']")
    cartPage = (By.XPATH, "//span[@id='attach-sidesheet-view-cart-button']")
    addQuantity = (By.XPATH, "//span[@class='a-icon a-icon-small-add']")
    itemRemovedCart = (By.XPATH, "//span[@class='a-size-base sc-list-item-removed-msg-text-delete']")
    cartItems = (By.XPATH, "//div[@data-csa-c-owner='CartX']")
    cartTotal = (By.XPATH, "//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap']")

    def verify_elements_visibility(self, locator):
        element_to_show = WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, locator)))

    def add_to_cart_button(self):
        log = self.get_logger()
        try:
            # Try the preferred locator first (the one that usually works)
            clickCart = self.driver.find_element(*addToCart.cart)
            log.info("Clicking on Add to Cart button (first attempt)")
            clickCart.click()

        except Exception as e:  # Handle exceptions if the first locator fails
            log.warning(f"First locator failed: {e}. Trying alternative locator.")
            try:
                clickCart2 = self.driver.find_element(*addToCart.alternative_locator)
                # Example alternative locator
                log.info("Clicking on Add to Cart button (second attempt)")
                clickCart2.click()
            except Exception as e2:
                log.error(f"Both locators failed: {e2}")
                raise  # Re-raise the exception to signal a failure.

    def price_added_cart(self):
        log = self.get_logger()
        cartPrice = self.driver.find_element(*addToCart.priceAdded)
        log.info(f"Price in cart: {cartPrice.text}")
        return cartPrice.text

    def cart_page(self):
        log = self.get_logger()
        cartPage = "//span[@id='attach-sidesheet-view-cart-button']"
        self.verify_elements_visibility(cartPage)
        go_to_Cart = self.driver.find_element(By.XPATH, cartPage)
        log.info("Navigating to Cart Page")
        go_to_Cart.click()

    def modify_cart_add(self):
        log = self.get_logger()
        addQuantity = self.driver.find_element(*addToCart.addQuantity)
        log.info("Increasing Cart Quantity")
        addQuantity.click()
        visible_delete = "//input[@value='Delete']"
        self.verify_elements_visibility(visible_delete)

    def verify_cart_modification(self):
        log = self.get_logger()
        po = PriceOperations()
        getCartTotal = self.driver.find_elements(*addToCart.cartTotal)[0].text
        cart_total = po.extract_price(getCartTotal)
        total = 0

        try:
            cart_items = self.driver.find_elements(*addToCart.cartItems)
            if len(cart_items) == 0:
                log.warning("No items found in the cart.")
                assert False, "No items found in the cart."

            for cart_item in cart_items:
                cartPrice = cart_item.get_attribute('data-price')
                cartQuantity = cart_item.get_attribute('data-quantity')
                if cartPrice is None or cartQuantity is None:
                    log.warning("data-price or data-quantity attribute is missing for a cart item.")
                    continue  # Skip to the next item

                try:
                    item_total = int(cartQuantity) * int(cartPrice)
                    total += item_total  # Accumulate the item total
                except ValueError:
                    log.error(f"Could not convert price or quantity to integer for item")
                    assert False, f"Invalid price or quantity format for item"

        except NoSuchElementException:
            log.error("Cart items element not found.")
            assert False, "Cart items element not found."

        assert total == cart_total, "Cart Total is incorrect"
        log.info(f"Calculated Total: {total}, Cart Total: {cart_total}")

    def modify_cart_reduce(self):
        log = self.get_logger()
        lowerQuantity = "//span[@class='a-icon a-icon-small-remove']"
        self.verify_elements_visibility(lowerQuantity)
        reduce_cart_item = self.driver.find_element(By.XPATH, lowerQuantity)
        log.info("Reducing Cart Quantity")
        reduce_cart_item.click()
        visible_delete = "//input[@value='Delete']"
        self.verify_elements_visibility(visible_delete)

    def delete_cart(self):
        log = self.get_logger()
        visible_delete = "//input[@value='Delete']"
        self.verify_elements_visibility(visible_delete)
        empty_cart = self.driver.find_element(By.XPATH, visible_delete)
        log.info("Clicking on Delete button")
        empty_cart.click()
        cart_empty = self.driver.find_element(*addToCart.itemRemovedCart)
        cart_empty_message = cart_empty.text
        log.info(f"Cart Deletion Message: {cart_empty_message}")
        return cart_empty_message




