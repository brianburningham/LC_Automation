import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class testFixture(unittest.TestCase):
    def setUp(self):
        url = "https://staging.linqconnect.com/";
        options = Options();
        options.binary_location = "C:\webdriver\chrome-win64\chrome.exe";
        service = Service(executable_path="C:\webdriver\chrome\chromedriver.exe");
        self.driver = webdriver.Chrome(
            #options=options,
            #service=
        );
        self.driver.get(url);
        self.driver.maximize_window();
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'mealApplicationStartButton'))
            )
        finally:
            return;

    def tearDown(self):
        self.driver.quit();
        return;

if __name__ == '__main__':
    unittest
