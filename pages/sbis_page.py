from utils.locator import *
from .base_page import BasePage


class SbisPage(BasePage):
    def __init__(self, driver):
        self.locator = SbisPageLocators
        super().__init__(driver)

    def click_contacts(self):
        self.find_element(*self.locator.CONTACTS).click()

    def click_tenzor(self):
        self.find_element(*self.locator.TENZOR).click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    def check_region(self):
        return self.find_element(*self.locator.REGION).text

    def click_region(self):
        self.find_element(*self.locator.REGION).click()

    def change_region(self):
        self.find_element(*self.locator.KAMCHATKA).click()

    def get_partner(self):
        return self.find_element(*self.locator.PARTNER).text

    def check_updated_data(self):
        correct_region = self.check_region() == "Камчатский край"
        correct_url = "kamchatskij" in self.driver.current_url
        correct_partner = "Нижний Новгород" != self.get_partner()
        correct_title = "Камчатский" in self.driver.title
        return correct_region, correct_url, correct_partner, correct_title

    def go_to_downloads(self):
        self.find_element(*self.locator.DOWNLOAD_PAGE).click()

    def click_download(self):
        self.find_element(*self.locator.DOWNLOAD).click()
