import pytest
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions
from selenium import webdriver
from TestData.HomePage_Data import HomePageData
from config import Config

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="select browser: chrome or firefox or edge"
    )
    parser.addoption(
        "--headless", action="store", default="false", help="on ui: true or false"
    )

def get_driver(request):
    browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    # Chrome Browser
    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")

        # Extra options as parameters     
        options.add_argument("--start-maximized")   # open browser full screen
        options.add_argument("--disable-notifications")  # disable pop-ups
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)
    
    # Firefox Browser
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        
        # Extra options as parameters     
        options.add_argument("--start-maximized")   # open browser full screen
        options.add_argument("--disable-notifications")  # disable pop-ups
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Firefox(options=options)
    
    # Edge Browser
    elif browser == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        
        # Extra options as parameters     
        options.add_argument("--start-maximized")   # open browser full screen
        options.add_argument("--disable-notifications")  # disable pop-ups
        options.add_argument("--window-size=1920,1080")
        
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
    driver.maximize_window()

    return driver

@pytest.fixture(scope="class", params=HomePageData.test_home_data)
def setup(request):
    driver = get_driver(request)
    data = request.param
    driver.get(Config.BASE_URL)
    request.cls.driver = driver
    request.cls.test_home_data = data
    yield
    driver.quit()

@pytest.fixture(scope="function", params=HomePageData.test_home_data_multiple)
def setup2(request):
    driver = get_driver(request)
    data = request.param
    driver.get(Config.BASE_URL)
    request.cls.driver = driver
    request.cls.test_multiple_data = data
    yield
    driver.quit()