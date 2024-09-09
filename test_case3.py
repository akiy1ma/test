import pytest
from selenium import webdriver
from page import SbisPage
import os
import time

driver = webdriver.Chrome()
driver.get("https://sbis.ru/")

sbis = SbisPage(driver)


def test_download():
    sbis = SbisPage(driver)
    sbis.go_to_downloads()
    sbis.click_download()
    time.sleep(20)
    file_path = os.path.join(os.getcwd(), "sbisplugin-setup-web.exe")
    assert os.path.exists(file_path) and round(os.path.getsize(file_path) / 1024 / 1024, 2)
