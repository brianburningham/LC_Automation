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
    def test_AutoPay_Single_NonShared(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.click_on(self.driver, 'addAutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/01NewAutopay.png');
        step.click_on(self.driver, 'autoPayDistrictSelect');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/02DistrictDropdown.png');
        step.click_on(self.driver, 'autoPay - TITAN Unified School District')
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/03DistrictSelected.png');
        step.click_on(self.driver, 'autoPayStudentSelectionSingle');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/04StudentDropdown.png');
        step.click_on(self.driver, 'autoPay - Harry Potter');
        #step.click_by_class_name(self.driver, 'cdk-overlay-container');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/05StudentSelected.png');
        step.insert_text_by_id(self.driver, 'autoPaySlideOutAmountInput', '10');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/06AmountSet.png');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/08FrequencySelected.png');
        step.insert_text_by_id(self.driver, 'autoPaySlideOutFrequencyAmountInput', '150');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/09BelowBalanceSet.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/10Save.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.scroll_to_by_id(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/11ConfirmSave.png');
        step.scroll_to_by_id(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/12AutoPayCard.png');
        # Clean up - remove the newly created autopay
        step.click_on(self.driver, 'autoPayDeleteButton-0');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/13ConfirmDelete.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.scroll_to_by_id(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/14EmptyAutoPayCard.png');
        return;

    @pytest.mark.release
    def test_AutoPay_Single_Shared(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.click_on(self.driver, 'addAutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/01NewAutopay.png');
        step.click_on(self.driver, 'autoPayDistrictSelect');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/02DistrictDropdown.png');
        step.click_on(self.driver, 'autoPay - TITAN Unified School District')
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/03DistrictSelected.png');
        step.click_on(self.driver, 'autoPayStudentSelectionSingle');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/04StudentDropdown.png');
        step.click_on(self.driver, 'autoPay - Ron Weasley,Ginny Weasley');
        #step.click_by_class_name(self.driver, 'cdk-overlay-container');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/05StudentSelected.png');
        step.insert_text_by_id(self.driver, 'autoPaySlideOutAmountInput', '10');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/06AmountSet.png');
        #step.click_on(self.driver, 'autoPaySlideOutFrequencySelect')
        #step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/07FrequencyDropdown.png');
        #step.click_on(self.driver, 'autoPaySLideOutFrequencyOption-0')
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/08FrequencySelected.png');
        step.insert_text_by_id(self.driver, 'autoPaySlideOutFrequencyAmountInput', '150');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/09BelowBalanceSet.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/10Save.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.scroll_to_by_id(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/11ConfirmSave.png');
        step.scroll_to_by_id(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/12AutoPayCard.png');
        # Clean up - remove the newly created autopay
        step.click_on(self.driver, 'autoPayDeleteButton-0');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/13ConfirmDelete.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.scroll_to_by_id(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/14EmptyAutoPayCard.png');
        return;

    @pytest.mark.release
    def test_AutoPay_Multiple_SharedAndNonShared(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.click_on(self.driver, 'addAutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/01NewAutopay.png');
        step.click_on(self.driver, 'autoPayDistrictSelect');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/02DistrictDropdown.png');
        step.click_on(self.driver, 'autoPay - TITAN Unified School District')
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/03DistrictSelected.png');
        step.click_on(self.driver, 'frecuency-tipe - Weekly');
        step.click_on(self.driver, 'autoPayStudentSelectionMultiple');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/04StudentDropdown.png');
        step.click_on(self.driver, 'autoPay - Ron Weasley,Ginny Weasley');
        step.click_on(self.driver, 'autoPay - Harry Potter');
        step.click_by_class_name(self.driver, 'cdk-overlay-container');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/05StudentSelected.png');
        step.insert_text_by_id(self.driver, 'autoPaySlideOutAmountInput', '10');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/06AmountSet.png');
        step.click_on(self.driver, 'autoPaySlideOutWeeklySelect')
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/07FrequencyDropdown.png');
        step.click_on(self.driver, 'autoPaySlideOutWeeklyOption-0')
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/08FrequencySelected.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/10Save.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.scroll_to_by_id(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/11ConfirmSave.png');
        step.scroll_to_by_id(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/12AutoPayCard.png');
        # Clean up - remove the newly created autopay
        step.click_on(self.driver, 'autoPayDeleteButton-0');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/13ConfirmDelete.png');
        step.click_on(self.driver, 'dialog-confirm');
        #step.click_on(self.driver, 'autoPayDeleteButton-0');
        #step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/13ConfirmDelete2.png');
        #step.click_on(self.driver, 'dialog-confirm');
        step.scroll_to_by_id(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/14EmptyAutoPayCard.png');
        return;

    @pytest.mark.release
    def test_AutoPay_Multiple_NonShared(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.click_on(self.driver, 'addAutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/01NewAutopay.png');
        step.click_on(self.driver, 'autoPayDistrictSelect');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/02DistrictDropdown.png');
        step.click_on(self.driver, 'autoPay - TITAN Unified School District')
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/03DistrictSelected.png');
        step.click_on(self.driver, 'frecuency-tipe - Weekly');
        step.click_on(self.driver, 'autoPayStudentSelectionMultiple');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/04StudentDropdown.png');
        step.click_on(self.driver, 'autoPay - Claire Wise');
        step.click_on(self.driver, 'autoPay - Harry Potter');
        step.click_by_class_name(self.driver, 'cdk-overlay-container');
        step.scroll_to_by_id(self.driver, 'autoPayDistrictSelect');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/05StudentSelected.png');
        step.insert_text_by_id(self.driver, 'autoPaySlideOutAmountInput', '10');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/06AmountSet.png');
        step.click_on(self.driver, 'autoPaySlideOutWeeklySelect')
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/07FrequencyDropdown.png');
        step.click_on(self.driver, 'autoPaySlideOutWeeklyOption-0')
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/08FrequencySelected.png');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/09BelowBalanceSet.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/10Save.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.scroll_to_by_id(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/11ConfirmSave.png');
        step.scroll_to_by_id(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/12AutoPayCard.png');
        # Clean up - remove the newly created autopay
        step.click_on(self.driver, 'autoPayDeleteButton-0');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/13ConfirmDelete.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.scroll_to_by_id(self.driver, 'chevron-button-AutoPay');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/14EmptyAutoPayCard.png');
        return;


if __name__ == '__main__':
    unittest.main()
