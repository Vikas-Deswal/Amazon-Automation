from selenium.common import NoSuchElementException
from utilities.BasePage import BaseActions
from pageObjects.locators import AddCartLocators


class addToCart(BaseActions):

    def add_to_cart_button(self):
        log = self.get_logger()
        try:
            # Try the preferred locator first (the one that usually works)
            self.element_is_visible(AddCartLocators.cart)
            clickCart = self.driver.find_element(*AddCartLocators.cart)
            log.info("Clicking on Add to Cart button (first attempt)")
            clickCart.click()

        except Exception as e:  # Handle exceptions if the first locator fails
            log.warning(f"First locator failed: {e}. Trying alternative locator.")
            try:
                self.element_is_visible(AddCartLocators.alternative_locator)
                clickCart2 = self.driver.find_element(*addToCart.alternative_locator)
                # Example alternative locator
                log.info("Clicking on Add to Cart button (second attempt)")
                clickCart2.click()
            except Exception as e2:
                log.error(f"Both locators failed: {e2}")
                raise  # Re-raise the exception to signal a failure.

        self.element_is_visible(AddCartLocators.actualCart)
        goToCart = self.driver.find_element(*AddCartLocators.actualCart)
        goToCart.click()

    def price_added_cart(self):
        log = self.get_logger()
        self.element_is_visible(AddCartLocators.priceAdded)
        cartPrice = self.driver.find_element(*AddCartLocators.priceAdded)
        log.info(f"Price in cart: {cartPrice.text}")
        return cartPrice.text

    def modify_cart_add(self):
        log = self.get_logger()
        self.element_is_visible(AddCartLocators.addQuantity)
        increase_cart = self.driver.find_element(*AddCartLocators.addQuantity)
        log.info("Increasing Cart Quantity")
        increase_cart.click()
        self.element_is_visible(AddCartLocators.visible_delete)

    def verify_cart_modification(self):
        log = self.get_logger()
        self.element_is_visible(AddCartLocators.cartTotal)
        getCartTotal = self.driver.find_elements(*AddCartLocators.cartTotal)[0].text
        cart_total = self.extract_price(getCartTotal)
        total = 0

        try:
            self.element_is_visible(AddCartLocators.cartItems)
            cart_items = self.driver.find_elements(*AddCartLocators.cartItems)
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
        self.element_is_visible(AddCartLocators.lowerQuantity)
        reduce_cart_item = self.driver.find_element(*AddCartLocators.lowerQuantity)
        log.info("Reducing Cart Quantity")
        reduce_cart_item.click()
        self.element_is_visible(AddCartLocators.visible_delete)

    def delete_cart(self):
        log = self.get_logger()
        empty_cart = self.element_clickable(AddCartLocators.visible_delete)
        log.info("Clicking on Delete button")
        empty_cart.click()

        self.element_is_visible(AddCartLocators.itemRemovedCart)
        cart_empty = self.driver.find_element(*AddCartLocators.itemRemovedCart)
        cart_empty_message = cart_empty.text
        log.info(f"Cart Deletion Message: {cart_empty_message}")
        return cart_empty_message




