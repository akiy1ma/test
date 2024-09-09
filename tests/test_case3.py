from pages.sbis_page import SbisPage
import os
import time


def test_download(driver):
    sbis = SbisPage(driver)
    sbis.go_to_downloads()
    sbis.click_download()
    time.sleep(10)
    file_path = os.path.join(os.getcwd(), "sbisplugin-setup-web.exe")
    assert os.path.exists(file_path) and round(os.path.getsize(file_path) / 1024 / 1024, 2)
