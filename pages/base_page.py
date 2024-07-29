import allure
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Открыть браузер')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Нахождение видимого элемента')
    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Нахождение видимых элементов')
    def element_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Нахождения представленного элемента')
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Нахождение представленных элементов')
    def element_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Нахождение невидимости элемента')
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Нахождение кликабельности элемента')
    def element_is_clickable(self, locator, timeout=8):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Переход к определенному элементу')
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step('Получение url')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Получение заголовка')
    def get_title(self):
        return self.driver.title

