from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.sbis_page import SbisPage
import os
import time

chrome_options = Options()
download_dir = os.getcwd()

prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}

chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://sbis.ru/")

sbis = SbisPage(driver)


def test_download():
    sbis = SbisPage(driver)
    sbis.go_to_downloads()
    sbis.click_download()
    time.sleep(20)
    file_path = os.path.join(os.getcwd(), "sbisplugin-setup-web.exe")
    assert os.path.exists(file_path) and round(os.path.getsize(file_path) / 1024 / 1024, 2)
