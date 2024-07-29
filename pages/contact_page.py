import allure
from locators.locators import ContactPageLocators
from pages.base_page import BasePage


class ContactPage(BasePage):

    locators = ContactPageLocators()

    @allure.step('Получение текущего региона')
    def get_current_region(self):
        return self.element_is_visible(self.locators.REGION_SELECTOR).text

    @allure.step('Выбор региона')
    def select_region(self):
        self.element_is_visible(self.locators.REGION_SELECTOR).click()
        self.element_is_clickable(self.locators.REGION_OPTION).click()

    @allure.step('Получение список партнеров')
    def get_partners_list(self):
        return self.element_are_present(self.locators.PARTNERS_LIST)

    # Можно использовать в будущем для проверки корректности списка партнеров
    @allure.step('Получение текста по списку партнеров')
    def get_all_partner_titles(self):
        elements = self.get_partners_list()
        return [element.get_attribute("title") for element in elements]


