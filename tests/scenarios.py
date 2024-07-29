import allure
from time import sleep
from pages.home_page import HomePage
from pages.tensor_page import TensorPage
from pages.contact_page import ContactPage
from utils.config import BASE_URL, TENSOR_URL, CONTACTS_URL

@allure.feature('Проверка тензор.ру')
@allure.story('Первый сценарий')
def test_first_scenario(driver):
    home_page = HomePage(driver, BASE_URL)

    with allure.step('Открыть главную страницу и перейти в раздел "Контакты"'):
        home_page.open()
        home_page.click_contacts_link()
        assert "Контакты" in driver.title, "Не удалось открыть страницу 'Контакты'"

    with allure.step('Кликнуть по баннеру "Тензор" на странице "Контакты"'):
        home_page.click_tensor_logo()
        assert len(driver.window_handles) == 2, "Новое окно не открылось"
        driver.switch_to.window(driver.window_handles[1])
        assert "tensor.ru" in driver.current_url, "Не удалось открыть сайт Тензор"

    tensor_page = TensorPage(driver, TENSOR_URL)

    with allure.step('Проверить наличие блока "Сила в людях" на сайте Тензор'):
        assert tensor_page.is_power_in_people_block_present() == 'Сила в людях', "Блок 'Сила в людях' отсутствует или текст не совпадает"

    with allure.step('Перейти по ссылке "Подробнее" в блоке "Сила в людях"'):
        tensor_page.click_more_info_link()
        assert driver.current_url == "https://tensor.ru/about", "URL не изменился на https://tensor.ru/about"

    with allure.step('Проверить, что все изображения в разделе "Работаем" имеют одинаковые размеры'):
        assert tensor_page.verify_work_images_dimensions(), "Изображения разного размера"

@allure.feature("Проверка страницы контактов")
@allure.story("Второй сценарий")
def test_second_scenario(driver):
    home_page = HomePage(driver, BASE_URL)

    with allure.step("Открытие домашней страницы"):
        home_page.open()

    with allure.step("Переход на страницу конкатов"):
        home_page.click_contacts_link()

    contact_page = ContactPage(driver, CONTACTS_URL)

    with allure.step("Проверка изначального региона и списка партнеров"):
        assert "Республика Марий Эл" in contact_page.get_current_region(), "Изначальный регион не корректен"
        assert contact_page.get_partners_list(), "Список партнеров не представлен"

    with allure.step("Смена региона на Камчатский край"):
        contact_page.select_region()

    sleep(1)
    # Очень быстро работает, парсит еще старый регион поэтому тут слип на 1 сек
    with allure.step("Verify Selected Region and Updated Partners List"):
        assert "Камчатский край" in contact_page.get_current_region(), "Выбранный регион не корректен"


    with allure.step("Проверка url и заголовка"):
        assert "kamchatskij" in contact_page.get_url().lower(), "URL не содержит регион"
        assert "Камчатский край" in contact_page.get_title(), "Заголовок не содержит выбранный регион"