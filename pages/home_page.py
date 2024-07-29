import allure
from locators.locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    locators = HomePageLocators()
    @allure.step('Переход на страницу контактов')
    def click_contacts_link(self):
        self.element_is_clickable(self.locators.CONTACTS_LINK).click()
    @allure.step('Клик на лого тензор')
    def click_tensor_logo(self):
        self.element_is_clickable(self.locators.TENSOR_LOGO).click()
