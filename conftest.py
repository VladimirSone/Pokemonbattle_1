import pytest
from selenium import webdriver
from url import URL

#  фикстура веб-драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.window('--window-size=1920,1080')
    driver.get(URL.BASE_URL)
    yield driver
    driver.quit()