from selenium.webdriver.common.by import By
from utilities.logging import Logger


class ProductOverviewPage(Logger):
    productTitle = (By.XPATH, "//span[@id='productTitle']")
    productPrice = (By.XPATH, "//span[@class='a-price-whole']")
    rating = (By.XPATH, "//span[@id='acrPopover']")
    customerReviewTotal = (By.XPATH, "//span[@id='acrCustomerReviewText']")
    featuresList = (By.XPATH, "//div[@id='featurebullets_feature_div']")
    productImages = (By.XPATH,"//li[@class='a-spacing-small item imageThumbnail a-declarative']")

    def __init__(self, driver):
        self.driver = driver

    def product_title(self):
        log = self.get_logger()
        try:
            title = self.driver.find_element(*ProductOverviewPage.productTitle)
            product_title = title.text
            log.info(f"Product title is {product_title}")
            return product_title
        except Exception as e:
            log.error(f"Error fetching title: {e}")
            return "Product Title is not found"

    def product_price(self):
        log = self.get_logger()
        try:
            price = self.driver.find_elements(*ProductOverviewPage.productPrice)
            product_price = price[4].text
            log.info(f"Product Price is: {product_price}")
        except Exception as e:
            log.error(f"Error fetching price: {e}")
            return "Product price is not found"

    def product_ratings(self):
        log = self.get_logger()
        try:
            rating = self.driver.find_elements(*ProductOverviewPage.rating)
            customerRatingsTotal = self.driver.find_elements(*ProductOverviewPage.customerReviewTotal)
            rating_info = f"The product has been rated {rating[1].text} out of 5 stars, with a total of {customerRatingsTotal[1].text}"
            log.info(rating_info)
            return rating_info
        except Exception as e:
            log.error(f"Error fetching product ratings: {e}")
            return "Product Ratings is not found"

    def product_images(self):
        log = self.get_logger()
        try:
            product_images = self.driver.find_elements(*ProductOverviewPage.productImages)
            if len(product_images) > 0:
                log.info(str(len(product_images)) + " images are present")
            else:
                log.info("No images are present")
        except Exception as e:
            log.error(f"Error finding product images: {e}")
