from locator import *
from .base_page import BasePage


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
