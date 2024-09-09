import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
download_dir = os.getcwd()

prefs = {
    "download.default_directory": download_dir,  # Set download directory
    "download.prompt_for_download": False,       # Disable download prompt
    "download.directory_upgrade": True,          # Allow directory upgrade
    "safebrowsing.enabled": True                 # Disable security blocking
}

chrome_options.add_experimental_option("prefs", prefs)


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://sbis.ru/")
    yield driver
    driver.quit()
