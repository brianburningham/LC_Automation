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
    def test_OneTimePayment_AddToShared(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToShared/01AccountPage.png');
        step.click_on(self.driver, 'otherButton-HarryPotter');
        step.insert_text_by_id(self.driver, 'mealAccountBalanceAmountInput-HarryPotter', '15');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToShared/02AmountSet.png');
        step.click_on(self.driver, 'mealAccountBalanceAddButton');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToShared/03AddToShoppingCart.png');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToShared/04ShoppingCart.png');
        step.go_to_checkout(self.driver);
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToShared/05CheckOut.png');
        step.confirm_and_pay(self.driver);
        step.wait_for(self.driver, 'transaction-history-route');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToShared/06TransactionCompleted.png');
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToShared/07AccountPage.png');
        return;

    @pytest.mark.release
    def test_OneTimePayment_DonateToBuilding(self):
        ## Log into District Portal To find beginning amount for the building##
        step.log_into_district_portal(self.driver);
        step.get_building_balance(self.driver, '0011', '001');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToBuilding/10StartBalance.png')
        self.driver.close();
        # time.sleep(10);
        self.driver.switch_to.window(self.driver.window_handles[0]);
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.click_on(self.driver, 'feeditFowardDistrictSelect');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToBuilding/01DistrictDropdown.png');
        step.click_on(self.driver, '_Smoke Test Staging');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToBuilding/02DistrictSelected.png');
        step.click_on(self.driver, 'feeditForwardSchoolDropdown');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToBuilding/03SchoolDropdown.png');
        step.click_on(self.driver, 'School 1');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToBuilding/04SchoolSelected.png');
        step.insert_text_by_id(self.driver, 'feedItForwardAmount', '10');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToBuilding/05AmountSet.png');
        step.click_on(self.driver, 'feeditForwardSave');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToBuilding/06AddedToCart.png');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToBuilding/07ShoppingCart.png');
        step.go_to_checkout(self.driver);
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToBuilding/08Checkout.png');
        step.confirm_and_pay(self.driver);
        step.wait_for(self.driver, 'transaction-history-route');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToBuilding/09TransactionCompleted.png');
        ## Log into District Portal To find new amount for the building##
        step.log_into_district_portal(self.driver);
        step.get_building_balance(self.driver, '0011', '001');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToBuilding/11newBalance.png')
        return;

    @pytest.mark.release
    def test_OneTimePayment_DonateTo2Buildings(self):
        ## Log into District Portal To find beginning amount for the buildings ##
        step.log_into_district_portal(self.driver);
        step.get_building_balance(self.driver, '0011', '001');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/14StartBalance.png')
        step.get_building_balance(self.driver, '0011', '002');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/16StartBalance.png')
        self.driver.close();
        # time.sleep(10);
        self.driver.switch_to.window(self.driver.window_handles[0]);
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.click_on(self.driver, 'feeditFowardDistrictSelect');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/01DistrictDropdown.png');
        step.click_on(self.driver, '_Smoke Test Staging');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/02DistrictSelected.png');
        step.click_on(self.driver, 'feeditForwardSchoolDropdown');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/03SchoolDropdown.png');
        step.click_on(self.driver, 'School 1');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/04SchoolSelected.png');
        step.insert_text_by_id(self.driver, 'feedItForwardAmount', '10');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/05AmountSet.png');
        step.click_on(self.driver, 'feeditForwardSave');
        step.click_on(self.driver, 'linqConnectSheetCloseSheetX');
        ## 2nd Building
        step.click_on(self.driver, 'feeditFowardDistrictSelect');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/06DistrictDropdown.png');
        step.click_on(self.driver, '_Smoke Test Staging');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/07DistrictSelected.png');
        step.click_on(self.driver, 'feeditForwardSchoolDropdown');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/08SchoolDropdown.png');
        step.click_on(self.driver, 'School 2 - CEP');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/09SchoolSelected.png');
        step.insert_text_by_id(self.driver, 'feedItForwardAmount', '10');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/10AmountSet.png');
        step.click_on(self.driver, 'feeditForwardSave');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/11ShoppingCart.png');
        step.go_to_checkout(self.driver);
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/12Checkout.png');
        step.confirm_and_pay(self.driver);
        step.wait_for(self.driver, 'transaction-history-route');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/13TransactionCompleted.png');
        ## Log into District Portal To find new amount for the buildings ##
        step.log_into_district_portal(self.driver);
        step.get_building_balance(self.driver, '0011', '001');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/15NewBalance.png')
        step.get_building_balance(self.driver, '0011', '002');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddTo2Building/17NewBalance.png')
        return;

    @pytest.mark.release
    def test_OneTimePayment_AddToStudentAndBuilding(self):
        ## Log into District Portal To find beginning amount for the building ##
        step.log_into_district_portal(self.driver);
        step.get_building_balance(self.driver, '0011', '001');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/13StartBalance.png')
        self.driver.close();
        # time.sleep(10);
        self.driver.switch_to.window(self.driver.window_handles[0]);
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        ## Add to Building
        step.click_on(self.driver, 'feeditFowardDistrictSelect');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/01DistrictDropdown.png');
        step.click_on(self.driver, '_Smoke Test Staging');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/02DistrictSelected.png');
        step.click_on(self.driver, 'feeditForwardSchoolDropdown');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/03SchoolDropdown.png');
        step.click_on(self.driver, 'School 1');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/04SchoolSelected.png');
        step.insert_text_by_id(self.driver, 'feedItForwardAmount', '10');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/05AmountSet.png');
        step.click_on(self.driver, 'feeditForwardSave');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/06AddToCart.png');
        step.click_on(self.driver, 'linqConnectSheetCloseSheetX');
        ## Add Balance to student
        step.click_on(self.driver, 'otherButton-HarryPotter');
        step.insert_text_by_id(self.driver, 'mealAccountBalanceAmountInput-HarryPotter', '15');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/07StudentAmountSet.png');
        step.click_on(self.driver, 'mealAccountBalanceAddButton');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/08AddToCart.png');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/09ShoppingCart.png');
        step.go_to_checkout(self.driver);
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/10CheckOut.png');
        step.confirm_and_pay(self.driver);
        step.wait_for(self.driver, 'transaction-history-route');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/11TransactionCompleted.png');
        step.click_on(self.driver, 'global-header-product-button');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/12NewStudentBalance.png');
        ## Log into District Portal To find new amount for the buildings ##
        step.log_into_district_portal(self.driver);
        step.get_building_balance(self.driver, '0011', '001');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/14NewBalance.png')
        return;

    @pytest.mark.release
    def test_OneTimePayment_Remove_All(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        ## Add to Building
        step.click_on(self.driver, 'feeditFowardDistrictSelect');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/01DistrictDropdown.png');
        step.click_on(self.driver, '_Smoke Test Staging');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/02DistrictSelected.png');
        step.click_on(self.driver, 'feeditForwardSchoolDropdown');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/03SchoolDropdown.png');
        step.click_on(self.driver, 'School 1');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/04SchoolSelected.png');
        step.insert_text_by_id(self.driver, 'feedItForwardAmount', '10');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/05AmountSet.png');
        step.click_on(self.driver, 'feeditForwardSave');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/06AddToCart.png');
        step.click_on(self.driver, 'linqConnectSheetCloseSheetX');
        ## Add Balance to student
        step.click_on(self.driver, 'otherButton-HarryPotter');
        step.insert_text_by_id(self.driver, 'mealAccountBalanceAmountInput-HarryPotter', '15');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/07StudentAmountSet.png');
        step.click_on(self.driver, 'mealAccountBalanceAddButton');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/08AddToCart.png');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/09ShoppingCart.png');
        step.go_to_checkout(self.driver);
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/10CheckOut.png');
        ## Remove All
        step.click_on(self.driver, 'cartItemId-0-deleteButton');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/11RemoveConfirmation.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/12CheckOut.png');
        step.click_on(self.driver, 'cartItemId-0-deleteButton');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/13RemoveConfirmation.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/14EmptyCheckout.png');
        return;


if __name__ == '__main__':
    unittest.main()
