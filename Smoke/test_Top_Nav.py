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
import base
import common_steps as step, common_steps as When, common_steps as And, common_steps as Then


class MyTestCase(base.testFixture):
    @pytest.mark.release
    def test_Top_Nav_Profile(self):
        step.log_into_Staging(self.driver);
        step.click_on(self.driver, 'global-header-profile-button');
        step.take_screenshot(self.driver, 'Release/Top_Nav/Profile/01TopNav_ProfileDropDown.png');
        step.click_on(self.driver, 'global-header-select-profile');
        step.take_screenshot(self.driver, 'Release/Top_Nav/Profile/02ProfileGeneral.png');
        step.scroll_to_by_id(self.driver, 'chevron-button-communications-preference');
        step.take_screenshot(self.driver, 'Release/Top_Nav/Profile/03ProfileCommunication.png');
        step.scroll_to_by_id(self.driver, 'chevron-button-person-addresses-card');
        step.take_screenshot(self.driver, 'Release/Top_Nav/Profile/04ProfileContacts.png');
        step.scroll_to_by_id(self.driver, 'chevron-button-person-addresses-card');
        step.take_screenshot(self.driver, 'Release/Top_Nav/Profile/05ProfilePayment.png');
        step.click_on(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/Top_Nav/Profile/06ProfileAutoPay.png');
        return;

    @pytest.mark.release
    def test_Top_Nav_Notifications(self):
        step.log_into_Staging(self.driver);
        time.sleep(2);
        step.assert_by_id(self.driver, 'global-header-notification-button');
        step.click_on(self.driver, 'global-header-notification-button');
        step.assert_by_text(self.driver, 'Notifications');
        step.assert_by_text(self.driver, 'All Notifications');
        step.take_screenshot(self.driver, 'Release/Top_Nav/Notifications/notifications.png')
        return;

    @pytest.mark.release
    def test_Top_Nav_Add(self):
        step.log_into_Staging(self.driver);
        step.click_on(self.driver, 'link-person-button-navbar');
        step.take_screenshot(self.driver, 'Release/Top_Nav/Add/Add.png')
        return;

    @pytest.mark.release
    def test_Top_Nav_ShoppingCart(self):
        step.log_into_Staging(self.driver);
        step.click_on(self.driver, 'global-header-shopping-cart-button');
        step.take_screenshot(self.driver, 'Release/Top_Nav/ShoppingCart/ShoppingCart.png');
        return;

    @pytest.mark.release
    def test_Top_Nav_Contact(self):
        step.log_into_Staging(self.driver);
        step.click_on(self.driver, 'global-header-district-contact-info-button');
        step.take_screenshot(self.driver, 'Release/Top_Nav/Contact/Contact.png');
        return;

    @pytest.mark.release
    def test_Top_Nav_PendoHelp(self):
        step.log_into_Staging(self.driver);
        step.click_on(self.driver, 'global-header-pendo-help-button');
        step.take_screenshot(self.driver, 'Release/Top_Nav/Help/Help.png');
        return;


if __name__ == '__main__':
    unittest.main()
