import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
import parameterized
import time
import basetest
import common_steps as step, common_steps as When, common_steps as And, common_steps as Then, common_steps as Given


class MyTestCase(basetest.testFixture):
    @pytest.mark.testall
    def test_Registration_ui(self):
        When.click_on(self.driver, 'headerRegister');
        Then.should_see_text(self.driver, 'Welcome to LINQ Connect!')
        And.should_see_text(self.driver, 'Register');
        And.should_see_text(self.driver, 'Please complete fields to register a new account in LINQ Connect. Required fields are marked with *.')
        And.should_see_text(self.driver, 'I agree to the');
        And.should_see_text(self.driver, 'Terms of Service.');
        And.should_see_element(self.driver, 'firstName');
        And.should_see_element(self.driver, 'lastName');
        And.should_see_element(self.driver, 'email');
        And.should_see_element(self.driver, 'password');
        And.should_see_element(self.driver, 'confirmPassword');
        And.should_see_element(self.driver, 'languageSelector');
        And.should_see_element(self.driver, 'registrationBackButton');
        return;

    @pytest.mark.testall
    def test_Registration_requiredfieldmessage(self):
        When.click_on(self.driver, 'headerRegister');
        And.should_see_text(self.driver, 'Welcome to LINQ Connect!');
        And.click_on(self.driver, 'firstName');
        And.click_on(self.driver, 'lastName');
        And.click_on(self.driver, 'email');
        And.click_on(self.driver, 'password');
        And.click_on(self.driver, 'confirmPassword');
        Then.should_see_text(self.driver, 'First Name Required');
        And.should_see_text(self.driver, 'Last Name Required');
        And.should_see_text(self.driver, 'Invalid email format. Ex. yourname@gmail.com');
        And.should_see_text(self.driver, 'Password Required');
        return;

if __name__ == '__main__':
    unittest.main()
