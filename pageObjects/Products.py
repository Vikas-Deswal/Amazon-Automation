from selenium.webdriver.common.by import By
from pageObjects.locators import ProductLocators
from utilities.BasePage import BaseActions

class ProductOverviewPage(BaseActions):
    featuresList = (By.XPATH, "//div[@id='featurebullets_feature_div']")
    productImages = (By.XPATH,"//li[@class='a-spacing-small item imageThumbnail a-declarative']")

    def product_title(self):
        log = self.get_logger()
        try:
            self.element_is_visible(ProductLocators.productTitle)
            title = self.driver.find_element(*ProductLocators.productTitle)
            product_title = title.text
            log.info(f"Product title is {product_title}")
            return product_title
        except Exception as e:
            log.error(f"Error fetching title: {e}")
            return "Product Title is not found"

    def product_price(self):
        log = self.get_logger()
        try:
            self.element_is_visible(ProductLocators.productPrice)
            price = self.driver.find_elements(*ProductLocators.productPrice)
            product_price = price[4].text
            return product_price
        except Exception as e:
            log.error(f"Error fetching price: {e}")
            return "Product price is not found"

    def product_ratings(self):
        log = self.get_logger()
        try:
            self.element_is_visible(ProductLocators.rating)
            rating = self.driver.find_elements(*ProductLocators.rating)
            self.element_is_visible(ProductLocators.customerReviewTotal)
            customerRatingsTotal = self.driver.find_elements(*ProductLocators.customerReviewTotal)
            rating_info = f"The product has been rated {rating[1].text} out of 5 stars, with a total of {customerRatingsTotal[1].text}"
            log.info(rating_info)
            return rating_info
        except Exception as e:
            log.error(f"Error fetching product ratings: {e}")
            return "Product Ratings is not found"

    def product_images(self):
        log = self.get_logger()
        try:
            self.element_is_visible(ProductLocators.productImages)
            product_images = self.driver.find_elements(*ProductLocators.productImages)
            if len(product_images) > 0:
                log.info(str(len(product_images)) + " images are present")
                return len(product_images)
            else:
                log.info("No images are present")
        except Exception as e:
            log.error(f"Error finding product images: {e}")
