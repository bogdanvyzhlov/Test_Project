from selenium.webdriver.common.by import By

class HomePageLocators:
    CONTACTS_LINK = (By.CSS_SELECTOR, "a[href='/contacts']")
    TENSOR_LOGO = (By.CSS_SELECTOR, "a[href='https://tensor.ru/']")

class TensorPageLocators:
    POWER_IN_PEOPLE_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg .tensor_ru-Index__card-title.tensor_ru-pb-16")
    MORE_INFO_LINK = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg div:nth-child(1) > div > p:nth-child(4) > a")
    WORK_IMAGES = (By.CSS_SELECTOR, ".tensor_ru-About__block3 .s-Grid-container")


class ContactPageLocators:
    REGION_SELECTOR = (By.CSS_SELECTOR, "div:nth-child(2) > span > span")
    REGION_OPTION = (By.CSS_SELECTOR, ".sbis_ru-Region-Panel ul li:nth-child(43) > span")
    PARTNERS_LIST = (By.CSS_SELECTOR, ".sbisru-Contacts-List__item [title]")

