import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

@pytest.fixture(scope='function')
def driver():
    #На макбуке пришлось использовать локально
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    options = Options()
    options_chrome = webdriver.ChromeOptions()
    ua = UserAgent()
    user_agent = ua.random
    print(user_agent)
    options.add_argument(f'--user-agent={user_agent}')
    #options_chrome.add_argument('headless')
    driver = webdriver.Chrome(options=options_chrome)
    driver.maximize_window()
    yield driver
    driver.quit()