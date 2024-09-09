from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, *locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")


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


class TenzorPage(BasePage):
    def __init__(self, driver):
        self.locator = TenzorPageLocators
        super().__init__(driver)

    def close_cookie(self):
        self.find_element(*self.locator.CLOSE_COOKIES).click()

    def click_about(self):
        self.find_elements(*TenzorPageLocators.STRENGTH_LINK)[2].click()

    def get_block(self):
        return self.find_element(*TenzorPageLocators.STRENGTH_BLOCK).is_displayed()

    def check_img_sizes(self):
        def get_work_images():
            return self.find_elements(*TenzorPageLocators.WORK_IMAGES)

        imgs = get_work_images()
        for i in range(len(imgs) - 1):
            if (imgs[i].size['width'], imgs[i].size['height']) != \
                    (imgs[i + 1].size['width'], imgs[i + 1].size['height']):
                return False
        return True
