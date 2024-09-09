from pages.sbis_page import SbisPage
from utils.navigation import Navigation


def test_region(driver):
    Navigation.sbis = SbisPage(driver)
    Navigation.sbis.click_contacts()
    assert Navigation.sbis.check_region() == 'Нижегородская обл.'


def test_changing_region(driver):
    Navigation.sbis.click_region()
    Navigation.sbis.change_region()
    assert Navigation.sbis.check_updated_data()
