from selenium import webdriver
from pages.sbis_page import SbisPage

driver = webdriver.Chrome()
driver.get("https://sbis.ru/")

sbis = SbisPage(driver)


def test_region():
    sbis.click_contacts()
    assert sbis.check_region() == 'Нижегородская обл.'


def test_changing_region():
    sbis.click_region()
    sbis.change_region()
    assert sbis.check_updated_data()
