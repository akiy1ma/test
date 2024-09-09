from selenium.webdriver.common.by import By


class SbisPageLocators(object):
    CONTACTS = (By.LINK_TEXT, "Контакты")
    TENZOR = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img')
    REGION = (By.XPATH,
              '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div['
              '2]/span/span')
    KAMCHATKA = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')
    PARTNER = (By.ID, "city-id-2")
    DOWNLOAD_PAGE = (By.LINK_TEXT, "Скачать локальные версии")
    DOWNLOAD = (By.XPATH,
                '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div['
                '2]/div[2]/div/a')


class TenzorPageLocators(object):
    CLOSE_COOKIES = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div[2]/div[2]')
    STRENGTH_BLOCK = (
    By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div')
    STRENGTH_LINK = (By.LINK_TEXT, "Подробнее")
    WORK_IMAGES = (By.CLASS_NAME, "tensor_ru-About__block3-image-wrapper")
