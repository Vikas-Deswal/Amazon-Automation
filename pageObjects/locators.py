from selenium.webdriver.common.by import By

class HomePageLocators:
    search_box = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    submit_button = (By.XPATH, "//input[@id='nav-search-submit-button']")
    cart_icon = (By.XPATH, "//a[@id='nav-cart']")

class SearchResultLocators:
    items_list = (By.XPATH, "//div[@class='a-section a-spacing-small a-spacing-top-small']")
    item_name = (By.XPATH, "div/a/h2/span")
    link_to_overview = (By.XPATH, "//a[@class='a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal']")

class ProductLocators:
    productTitle = (By.XPATH, "//span[@id='productTitle']")
    productPrice = (By.XPATH, "//span[@class='a-price-whole']")
    rating = (By.XPATH, "//span[@id='acrPopover']")
    customerReviewTotal = (By.XPATH, "//span[@id='acrCustomerReviewText']")
    featuresList = (By.XPATH, "//div[@id='featurebullets_feature_div']")
    productImages = (By.XPATH, "//li[@class='a-spacing-small item imageThumbnail a-declarative']")

class AddCartLocators:
    cart = (By.XPATH, "(//input[@id='add-to-cart-button'])[2]")
    alternative_locator = (By.XPATH, "//input[@id='add-to-cart-button']")
    priceAdded = (By.XPATH, "//span[@class='a-price a-text-price sc-product-price sc-white-space-nowrap a-size-medium']")
    cartPage = (By.XPATH, "//span[@id='attach-sidesheet-view-cart-button']")
    actualCart = (By.XPATH, "//span[@id='sw-gtc']")
    addQuantity = (By.XPATH, "//span[@class='a-icon a-icon-small-add']")
    cartItems = (By.XPATH, "//div[@data-csa-c-owner='CartX']")
    cartTotal = (By.XPATH, "//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap']")
    visible_delete = (By.XPATH, "//input[@value='Delete']")
    lowerQuantity = (By.XPATH, "//span[@class='a-icon a-icon-small-remove']")
    itemRemovedCart = (By.XPATH, "//span[contains(@id, 'sc-list-item-removed-msg-text-delete')]")