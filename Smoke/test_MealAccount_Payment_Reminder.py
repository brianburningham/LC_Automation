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
    def test_Payment_Reminder(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.click_on(self.driver, 'paymentReminderDeleteButton-0');
        step.take_screenshot(self.driver, 'Release/PaymentReminder/01NotSet.png');
        step.click_on(self.driver, 'paymentReminderEditButton-0');
        step.insert_text_by_id(self.driver, 'paymentReminderAmountInput-0', '15');
        step.click_on(self.driver, 'paymentReminderSaveButton-0');
        step.take_screenshot(self.driver, 'Release/PaymentReminder/02SetPositive.png');
        step.click_on(self.driver, 'paymentReminderDeleteButton-0');
        step.click_on(self.driver, 'paymentReminderEditButton-0');
        step.click_on(self.driver, 'paymentReminderSaveButton-0');
        step.take_screenshot(self.driver, 'Release/PaymentReminder/03SetDefault.png');
        return;


if __name__ == '__main__':
    unittest.main()
