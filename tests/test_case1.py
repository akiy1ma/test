from pages.sbis_page import SbisPage
from pages.tenzor_page import TenzorPage
from utils.navigation import Navigation


def test_block_presence(driver):
    Navigation.sbis = SbisPage(driver)
    Navigation.sbis.click_contacts()
    Navigation.sbis.click_tenzor()

    Navigation.tenzor = TenzorPage(driver)
    Navigation.tenzor.close_cookie()

    assert Navigation.tenzor.get_block(), "Блок сила в людях отсутствует"


def test_about_page_url(driver):
    Navigation.tenzor.click_about()
    assert driver.current_url == "https://tensor.ru/about", "Ссылка некорректна"


def test_image_sizes(driver):
    assert Navigation.tenzor.check_img_sizes(), "Изображения разной высоты/ширины"
