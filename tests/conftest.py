import pytest
from selenium import webdriver
from TestData.HomePage_Data import HomePageData


@pytest.fixture(scope="class", params=HomePageData.test_home_data)
def setup(request):
    driver = webdriver.Chrome()
    data = request.param
    driver.get("https://www.amazon.in")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.test_home_data = data
    yield
    driver.quit()

@pytest.fixture(scope="function", params=HomePageData.test_home_data_multiple)
def setup2(request):
    driver = webdriver.Chrome()
    data = request.param
    driver.get("https://www.amazon.in")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.test_multiple_data = data
    yield
    driver.quit()