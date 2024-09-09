import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page import SbisPage, TenzorPage

chrome_options = Options()
download_dir = os.getcwd()

prefs = {
    "download.default_directory": download_dir,  # Set download directory
    "download.prompt_for_download": False,       # Disable download prompt
    "download.directory_upgrade": True,          # Allow directory upgrade
    "safebrowsing.enabled": True                 # Disable security blocking
}

chrome_options.add_experimental_option("prefs", prefs)


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://sbis.ru/")
    yield driver
    driver.quit()


class Navigation:
    sbis = SbisPage(driver)
    tenzor = TenzorPage(driver)


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

