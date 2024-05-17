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
    def test_Balance_Transfer(self):
        step.log_into_Staging(self.driver);
        step.take_screenshot(self.driver, 'Release/BalanceTransfer/07StartBalance.png')
        step.go_to_account_page(self.driver);
        step.scroll_to_by_id(self.driver, 'transferBalanceFromDropdown');
        step.take_screenshot(self.driver, 'Release/BalanceTransfer/01Blank.png')
        step.click_on(self.driver, 'transferBalanceFromDropdown');
        step.take_screenshot(self.driver, 'Release/BalanceTransfer/02FromList.png');
        step.click_on(self.driver, 'Harry Potter');
        step.take_screenshot(self.driver, 'Release/BalanceTransfer/03FromSelected.png');
        step.click_on(self.driver, 'transferBalanceToDropdown');
        step.take_screenshot(self.driver, 'Release/BalanceTransfer/04ToList.png');
        step.click_on(self.driver, 'Ron Weasley');
        step.take_screenshot(self.driver, 'Release/BalanceTransfer/04ToSelected.png');
        step.insert_text_by_id(self.driver, 'transferBalanceAmountInput', '10');
        step.take_screenshot(self.driver, 'Release/BalanceTransfer/05AmountSet.png');
        step.click_on(self.driver, 'transferBalanceTransferButton');
        step.take_screenshot(self.driver, 'Release/BalanceTransfer/06TransferCompleted.png');
        step.click_on(self.driver, 'global-header-product-button');
        step.take_screenshot(self.driver, 'Release/BalanceTransfer/08newBalance.png')
        return;


if __name__ == '__main__':
    unittest.main()
