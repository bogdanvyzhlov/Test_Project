import allure
from locators.locators import TensorPageLocators
from pages.base_page import BasePage


class TensorPage(BasePage):

    locators = TensorPageLocators()
    @allure.step('Проверка наличия блока сила в людях')
    def is_power_in_people_block_present(self):
       element=self.element_is_present(self.locators.POWER_IN_PEOPLE_BLOCK)
       self.go_to_element(element)
       return element.text
    @allure.step('Клик на подробнее')
    def click_more_info_link(self):
        self.element_is_clickable(self.locators.MORE_INFO_LINK).click()
    @allure.step('Проверка размеров изображения')
    def verify_work_images_dimensions(self):
        images = self.element_are_present(self.locators.WORK_IMAGES)
        if not images:
            return False
        first_image = images[0]
        width = first_image.get_attribute("width")
        height = first_image.get_attribute("height")
        for img in images:
            if img.get_attribute("width") != width or img.get_attribute("height") != height:
                return False
        return True
