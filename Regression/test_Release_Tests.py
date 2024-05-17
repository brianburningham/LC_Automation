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
    def test_MealApp_Eng_noAuth(self):
        When.click_on(self.driver, 'mealApplicationStartButton');
        And.insert_text_by_id(self.driver, 'districtSingleSelect', '_Smoke Test Staging');
        time.sleep(2);
        And.click_on(self.driver, 'cdk-overlay-0');
        #self.driver.switch_to_active_element().send_keys(Keys.ENTER);
        #time.sleep(2);
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/01MealApp_eng_GeneralInfo.png');
        step.click_on(self.driver, 'generalInfoNext')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/02MealApp_eng_AdditionalQuestions.png');
        step.click_on(self.driver, 'additionalQuestionsFormNext')
        step.take_screenshot(self.driver,
                             'Release/MealApp/MealApp_noAuth/Eng/03MealApp_eng_Letter.png');
        step.click_on(self.driver, 'letterToHouseholdNext')
        step.click_by_xpath(self.driver, '//*[@id="null"]/div[2]/div/button');
        step.insert_text_by_id(self.driver, 'firstNameStudentForm', 'Brian');
        step.insert_text_by_id(self.driver, 'lastNameStudentForm', 'Student');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/04MealApp_eng_Student.png');
        step.insert_text_by_id(self.driver, 'studentIncome', '1000')
        #time.sleep(5);
        step.click_on(self.driver, 'studentsNext');
        step.insert_text_by_id(self.driver, 'numberOfHouseholdMembers', '2');
        step.scroll_to_by_id(self.driver, 'linqConnectSheetConfirmButton')
        step.click_on(self.driver, 'newAdult');
        step.insert_text_by_id(self.driver, 'firstName', 'Brian');
        step.insert_text_by_id(self.driver, 'lastName', 'Burningham');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/05MealApp_eng_household_slideout.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/06MealApp_eng_household.png');
        step.click_on(self.driver, 'householdNext');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/07MealApp_eng_review1.png');
        step.scroll_to_by_id(self.driver, 'editHousehold')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/08MealApp_eng_review2.png');
        step.scroll_to_by_id(self.driver, 'reviewNext');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/09MealApp_eng_review3.png');
        step.click_on(self.driver, 'reviewNext');
        step.insert_text_by_id(self.driver, 'signedBy', 'Brian Burningham');
        step.click_by_xpath(self.driver, '//*[@id="agreeToTerms-1"]/label');
        step.click_on(self.driver, 'noSSN');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/10MealApp_eng_Submit1.png');
        step.scroll_to_by_id(self.driver, 'submit');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/11MealApp_eng_Submit2.png');
        step.click_on(self.driver, 'submit');
        #time.sleep(5);
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/12MealApp_eng_completed.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Welcome to LINQ Connect!');
        return;

    @pytest.mark.release
    def test_MealApp_Spa_noAuth(self):
        step.set_language_to(self.driver, 'Spanish');
        step.click_on(self.driver, 'mealApplicationStartButton');
        step.insert_text_by_id(self.driver, 'districtSingleSelect', '_Smoke Test Staging');
        time.sleep(2);
        And.click_on(self.driver, 'cdk-overlay-1');
        #self.driver.switch_to_active_element().send_keys(Keys.ENTER);
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/01MealApp_spa_GeneralInfo.png');
        step.click_on(self.driver, 'generalInfoNext')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/02MealApp_spa_AdditionalQuestions.png');
        step.click_on(self.driver, 'additionalQuestionsFormNext')
        step.take_screenshot(self.driver,
                             'Release/MealApp/MealApp_noAuth/Spa/03MealApp_eng_Letter.png');
        step.click_on(self.driver, 'letterToHouseholdNext')
        step.click_by_xpath(self.driver, '//*[@id="null"]/div[2]/div/button');
        step.insert_text_by_id(self.driver, 'firstNameStudentForm', 'Brian');
        step.insert_text_by_id(self.driver, 'lastNameStudentForm', 'Student');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/04MealApp_spa_Student.png');
        step.insert_text_by_id(self.driver, 'studentIncome', '1000')
        step.click_on(self.driver, 'studentsNext');
        step.insert_text_by_id(self.driver, 'numberOfHouseholdMembers', '2');
        #step.scroll_to_by_id(self.driver, 'householdNext')
        step.wait_until_not_displayed(self.driver, 'cdk-overlay-pane');
        #step.wait_until_not_displayed(self.driver,
         #                             'mat-snack-bar-container ng-tns-c257-106 ng-trigger ng-trigger-state linq-snackbar--success mat-snack-bar-center ng-star-inserted');
        step.click_on(self.driver, 'newAdult');
        step.insert_text_by_id(self.driver, 'firstName', 'Brian');
        step.insert_text_by_id(self.driver, 'lastName', 'Burningham');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/05MealApp_spa_household_slideout.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/06MealApp_spa_household.png');
        step.click_on(self.driver, 'householdNext');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/07MealApp_spa_review1.png');
        step.scroll_to_by_id(self.driver, 'editHousehold')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/08MealApp_spa_review2.png');
        step.scroll_to_by_id(self.driver, 'reviewNext');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/09MealApp_spa_review3.png');
        step.click_on(self.driver, 'reviewNext');
        step.insert_text_by_id(self.driver, 'signedBy', 'Brian Burningham');
        step.click_by_xpath(self.driver, '//*[@id="agreeToTerms-1"]/label');
        step.click_on(self.driver, 'noSSN');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/10MealApp_spa_Submit1.png');
        step.scroll_to_by_id(self.driver, 'submit');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/11MealApp_spa_Submit2.png');
        step.click_on(self.driver, 'submit');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/12MealApp_spa_completed.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Welcome to LINQ Connect!');
        return;

    @pytest.mark.release
    def test_Add_to_Balance_MealBalanceCard(self):
        step.log_into_Staging(self.driver);
        step.click_on(self.driver, 'mealBalanceAddButton');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/01Meal_Balance_start_amount.png');
        step.insert_text_by_id(self.driver, 'mealAccountBalanceAmountInput-3', '10');
        step.click_on(self.driver, 'mealAccountBalanceAddButton');
        time.sleep(2);
        step.click_on(self.driver, 'global-header-shopping-cart-button');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/02Meal_Balance_Cart.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/03Meal_Balance_Checkout.png');
        step.wait_for(self.driver, 'checkout-confirm-pay');
        step.click_on(self.driver, 'checkout-confirm-pay');
        time.sleep(3)
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/04Meal_Balance_Complete1.png');
        time.sleep(3);
        step.click_on(self.driver, 'global-header-product-button');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/04Meal_Balance_Complete2.png');
        time.sleep(3);
        return;

    @pytest.mark.release
    def test_Add_to_Balance_MenuNav(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/01Meal_Balance_start_amount.png');
        step.insert_text_by_id(self.driver, 'mealAccountBalanceAmountInput-3', '10');
        step.click_on(self.driver, 'mealAccountBalanceAddButton');
        step.click_on(self.driver, 'global-header-shopping-cart-button');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/02Meal_Balance_Cart.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/03Meal_Balance_Checkout.png');
        step.wait_for(self.driver, 'checkout-confirm-pay');
        step.click_on(self.driver, 'checkout-confirm-pay');
        time.sleep(3)
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/04Meal_Balance_Complete1.png');
        time.sleep(3);
        step.click_on(self.driver, 'global-header-product-button');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/04Meal_Balance_Complete2.png');
        time.sleep(3);
        return;

    @pytest.mark.release
    def test_link_unlink_Student(self):
        step.log_into_Staging(self.driver);
        step.click_on(self.driver, 'link-person-button-navbar');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/01SlideOut.png');
        step.click_on(self.driver, 'personType');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/02SlideOut.png');
        step.click_on(self.driver, 'Student');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/03SlideOut.png');
        step.insert_text_by_id(self.driver, 'districtSelect', 'Titan Unified');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/04SlideOut.png');
        time.sleep(2);
        self.driver.switch_to_active_element().send_keys(Keys.ENTER);
        time.sleep(2);
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/05SlideOut.png');
        step.insert_text_by_id(self.driver, 'identifier', '1983');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/06SlideOut.png');
        step.insert_text_by_id(self.driver, 'firstName', 'Link');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/07SlideOut.png');
        step.insert_text_by_id(self.driver, 'lastName', 'Student');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/08SlideOut.png');
        step.insert_text_by_id(self.driver, 'dateOfBirth', '05/05/2008');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/09SlideOut.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        ## To Finish this, we need US 176232 completed. We'll scroll to the student card then we will remove it.
        step.click_on(self.driver, 'LinkStudent-personCardChevronButton-expandMore');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/10ExpandStudentCard.png');
        step.click_on(self.driver, 'LinkStudent-personCardKebab');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/11OpenKebob.png');
        step.click_on(self.driver, 'null');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/12StudentRemoved.png');
        return;

    @pytest.mark.release
    #Will be in Staging 8/15
    def test_link_unlink_Staff(self):
        step.log_into_Staging(self.driver);
        step.click_on(self.driver, 'link-person-button-navbar');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/01SlideOut.png');
        step.click_on(self.driver, 'personType');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/02SlideOut.png');
        step.click_on(self.driver, 'Staff');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/03SlideOut.png');
        step.insert_text_by_id(self.driver, 'districtSelect', 'Titan Unified');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/04SlideOut.png');
        time.sleep(2);
        self.driver.switch_to_active_element().send_keys(Keys.ENTER);
        time.sleep(2);
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/05SlideOut.png');
        step.insert_text_by_id(self.driver, 'identifier', 'sys-1983');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/06SlideOut.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.click_on(self.driver, 'LinkStaff-personCardChevronButton-expandMore');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/07ExpandStudentCard.png');
        step.click_on(self.driver, 'LinkStaff-personCardKebab');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/07OpenKebob.png');
        step.click_on(self.driver, 'null');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/07StudentRemoved.png');
        return;

    @pytest.mark.release
    def test_Payment_Reminder(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        #step.scroll_to_by_id(self.driver, 'chevron-button-PaymentReminder');
        step.click_on(self.driver, 'paymentReminderDeleteButton-0');
        step.take_screenshot(self.driver, 'Release/PaymentReminder/01NotSet.png');
        step.click_on(self.driver, 'paymentReminderEditButton-0');
        step.insert_text_by_id(self.driver, 'paymentReminderAmountInput-0', '15');
        step.click_on(self.driver, 'paymentReminderSaveButton-0');
        step.take_screenshot(self.driver, 'Release/PaymentReminder/02SetPositive.png');
        step.click_on(self.driver, 'paymentReminderEditButton-0');
        step.insert_text_by_id(self.driver, 'paymentReminderAmountInput-0', '-15');
        step.click_on(self.driver, 'paymentReminderSaveButton-0');
        step.take_screenshot(self.driver, 'Release/PaymentReminder/03SetNegative.png');
        step.click_on(self.driver, 'paymentReminderDeleteButton-0');
        step.click_on(self.driver, 'paymentReminderEditButton-0');
        step.click_on(self.driver, 'paymentReminderSaveButton-0');
        step.take_screenshot(self.driver, 'Release/PaymentReminder/03SetDefault.png');
        return;

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
        step.assert_by_text(self.driver, 'No New Notifications');
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

    @pytest.mark.release
    def test_Home_TermsofUse(self):
        step.log_into_Staging(self.driver);
        step.click_on(self.driver, 'global-header-hamburger-button')
        step.click_on(self.driver, 'termsOfUseButton');
        step.take_screenshot(self.driver, 'Release/Home/TermsofUse/01TermsofUse.png');
        step.click_by_xpath(self.driver, '//*[@id="dialog-close"]/span[1]/mat-icon');
        step.take_screenshot(self.driver, 'Release/Home/TermsofUse/02TermsofUseClosed.png');
        step.click_on(self.driver, 'termsOfUseButton');
        step.take_screenshot(self.driver, 'Release/Home/TermsofUse/03TermsofUse.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Release/Home/TermsofUse/03TermsofUseClosed.png');
        return;

    @pytest.mark.release
    def test_LINQ_Logo(self):
        step.log_into_Staging(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/LINQLogo/01Dashboard.png');
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/LINQLogo/02AccountPage.png');
        step.click_on(self.driver, 'global-header-product-button');
        step.text_is_displayed(self.driver, 'Dashboard');
        step.take_screenshot(self.driver, 'Release/Home/LINQLogo/03ReturntoDashboard.png');
        return;

    @pytest.mark.release
    def test_OneTimePayment_AddToShared(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToShared/01AccountPage.png');
        step.insert_text_by_id(self.driver, 'mealAccountBalanceAmountInput-4', '10');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToShared/02AmountSet.png');
        step.click_on(self.driver, 'mealAccountBalanceAddButton');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToShared/03AddToShoppingCart.png');
        step.open_shopping_cart(self.driver);
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
        step.open_shopping_cart(self.driver);
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
        step.open_shopping_cart(self.driver);
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
        #time.sleep(10);
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
        ## Add Balance to student
        step.scroll_to_by_id(self.driver, 'mealAccountBalanceAmountInput-3')
        step.insert_text_by_id(self.driver, 'mealAccountBalanceAmountInput-3', '10');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/07StudentAmountSet.png');
        step.click_on(self.driver, 'mealAccountBalanceAddButton');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/AddToStudentAndBuilding/08AddToCart.png');
        step.open_shopping_cart(self.driver);
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
        ## Add Balance to student
        step.insert_text_by_id(self.driver, 'mealAccountBalanceAmountInput-3', '10');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/07StudentAmountSet.png');
        step.click_on(self.driver, 'mealAccountBalanceAddButton');
        step.take_screenshot(self.driver, 'Release/OneTimePayment/RemoveAll/08AddToCart.png');
        step.open_shopping_cart(self.driver);
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
        step.click_on(self.driver, 'autoPayStudentSelection');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/04StudentDropdown.png');
        step.click_on(self.driver, 'autoPay - Harry Potter');
        step.click_by_class_name(self.driver, 'cdk-overlay-container');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/05StudentSelected.png');
        step.insert_text_by_id(self.driver, 'autoPaySlideOutAmountInput', '10');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/06AmountSet.png');
        step.click_on(self.driver, 'autoPaySlideOutFrequencySelect')
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleNonShared/07FrequencyDropdown.png');
        step.click_on(self.driver, 'autoPaySLideOutFrequencyOption-0')
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
        step.click_on(self.driver, 'autoPayStudentSelection');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/04StudentDropdown.png');
        step.click_on(self.driver, 'autoPay - Ron Weasley');
        step.click_by_class_name(self.driver, 'cdk-overlay-container');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/05StudentSelected.png');
        step.insert_text_by_id(self.driver, 'autoPaySlideOutAmountInput', '10');
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/06AmountSet.png');
        step.click_on(self.driver, 'autoPaySlideOutFrequencySelect')
        step.take_screenshot(self.driver, 'Release/AutoPay/SingleShared/07FrequencyDropdown.png');
        step.click_on(self.driver, 'autoPaySLideOutFrequencyOption-0')
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
        step.click_on(self.driver, 'autoPayStudentSelection');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/04StudentDropdown.png');
        step.click_on(self.driver, 'autoPay - Ron Weasley');
        step.click_on(self.driver, 'autoPay - Harry Potter');
        step.click_by_class_name(self.driver, 'cdk-overlay-container');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/05StudentSelected.png');
        step.insert_text_by_id(self.driver, 'autoPaySlideOutAmountInput', '10');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/06AmountSet.png');
        step.click_on(self.driver, 'autoPaySlideOutFrequencySelect')
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/07FrequencyDropdown.png');
        step.click_on(self.driver, 'autoPaySLideOutFrequencyOption-0')
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/08FrequencySelected.png');
        step.insert_text_by_id(self.driver, 'autoPaySlideOutFrequencyAmountInput', '150');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleSharedAndNonShared/09BelowBalanceSet.png');
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
        step.click_on(self.driver, 'autoPayStudentSelection');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/04StudentDropdown.png');
        step.click_on(self.driver, 'autoPay - Claire Wise');
        step.click_on(self.driver, 'autoPay - Harry Potter');
        step.click_by_class_name(self.driver, 'cdk-overlay-container');
        step.scroll_to_by_id(self.driver, 'autoPayDistrictSelect');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/05StudentSelected.png');
        step.insert_text_by_id(self.driver, 'autoPaySlideOutAmountInput', '10');
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/06AmountSet.png');
        step.click_on(self.driver, 'autoPaySlideOutFrequencySelect')
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/07FrequencyDropdown.png');
        step.click_on(self.driver, 'autoPaySLideOutFrequencyOption-0')
        step.take_screenshot(self.driver, 'Release/AutoPay/MultipleNonShared/08FrequencySelected.png');
        step.insert_text_by_id(self.driver, 'autoPaySlideOutFrequencyAmountInput', '150');
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

    @pytest.mark.release
    def test_History_FilterStudent(self):
        step.log_into_Staging(self.driver);
        step.go_to_history(self.driver);
        step.take_screenshot(self.driver, 'Release/History/FilterStudent/01History.png');
        step.click_by_xpath(self.driver, '//*[@id="null"]/div/ag-grid-angular/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/span/span');
        step.take_screenshot(self.driver, 'Release/History/FilterStudent/02Filter.png');
        step.click_by_xpath(self.driver, '//*[@id="null"]/div/ag-grid-angular/div/div[6]/div/div[1]/span[2]/span');
        step.take_screenshot(self.driver, 'Release/History/FilterStudent/03Filter.png');
        step.insert_text_by_id(self.driver, 'ag-145-input', 'Harry Potter');
        step.take_screenshot(self.driver, 'Release/History/FilterStudent/04Student.png');
        self.driver.find_element_by_id('ag-145-input').send_keys(Keys.ENTER);
        step.take_screenshot(self.driver, 'Release/History/FilterStudent/05StudentFilter.png');
        step.click_by_xpath(self.driver, '//*[@id="null"]/linq-table-filters/div/div/mat-chip')
        step.take_screenshot(self.driver, 'Release/History/FilterStudent/06FilterCleared.png');
        time.sleep(1);
        return;

    @pytest.mark.release
    def test_History_Pagination(self):
        step.log_into_Staging(self.driver);
        step.go_to_history(self.driver);
        step.take_screenshot(self.driver, 'Release/History/Pagination/01Page1.png');
        step.click_by_xpath(self.driver, '//*[@id="null"]/linq-table-footer/footer/div[2]/mat-paginator/div/div/div[2]/button[2]');
        step.take_screenshot(self.driver, 'Release/History/Pagination/02Page2.png');
        step.click_by_xpath(self.driver,
                            '//*[@id="null"]/linq-table-footer/footer/div[2]/mat-paginator/div/div/div[2]/button[2]');
        step.take_screenshot(self.driver, 'Release/History/Pagination/03Page3.png');
        step.click_by_xpath(self.driver,
                            '//*[@id="null"]/linq-table-footer/footer/div[2]/mat-paginator/div/div/div[2]/button[2]');
        step.take_screenshot(self.driver, 'Release/History/Pagination/04Page4.png')
        step.click_by_xpath(self.driver,
                            '//*[@id="null"]/linq-table-footer/footer/div[2]/mat-paginator/div/div/div[2]/button[2]');
        step.take_screenshot(self.driver, 'Release/History/Pagination/05Page5.png');
        step.click_by_xpath(self.driver,
                            '//*[@id="null"]/linq-table-footer/footer/div[2]/mat-paginator/div/div/div[2]/button[2]');
        step.take_screenshot(self.driver, 'Release/History/Pagination/06Page6.png');
        time.sleep(1);
        return;

    @pytest.mark.release
    def test_History_Transaction(self):
        step.log_into_Staging(self.driver);
        step.go_to_history(self.driver);
        step.click_by_xpath(self.driver, '//*[@id="null"]/div/ag-grid-angular/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[4]');
        step.take_screenshot(self.driver, 'Release/History/Transaction/01Transaction.png');
        return;

    @pytest.mark.release
    def test_History_Empty(self):
        step.click_on(self.driver, 'landingPageLoginButton');
        step.log_in_with(self.driver, 'brian_smoke_test@gmail.com', 'Titan123!');
        step.go_to_history(self.driver);
        step.take_screenshot(self.driver, 'Release/History/Empty/01Empty.png');
        return;

    @pytest.mark.release
    def test_IncomeForm_AddStudent(self):
        step.log_into_Staging(self.driver);
        step.go_to_income_form(self.driver);
        step.click_by_xpath(self.driver, '//*[@id="null"]/linq-table-header/header/div[2]/linq-buttons/div/button');
        step.insert_text_by_id(self.driver, 'firstName', 'Brian');
        step.insert_text_by_id(self.driver, 'lastName', 'Test');
        step.insert_text_by_id(self.driver, 'phone', '4355555555');
        step.click_on(self.driver, 'incomeFormGeneralNextButton');
        step.insert_text_by_id(self.driver, 'householdSize', '2');
        step.click_on(self.driver, 'newAdult');
        step.insert_text_by_id(self.driver, 'firstName', 'Brian');
        step.insert_text_by_id(self.driver, 'lastName', 'Test');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.click_on(self.driver, 'incomeFormHouseholdNextButton');
        step.click_by_xpath(self.driver, '//*[@id="null"]/div[2]/div/button');
        step.insert_text_by_id(self.driver, 'firstNameStudentForm', 'Brian');
        step.insert_text_by_id(self.driver, 'lastNameStudentForm', 'Student');
        step.click_on(self.driver, 'dateOfBirthStudentForm');
        step.take_screenshot(self.driver, 'Release/IncomeForm/AddStudent/AddStudent_DatePlacement.png')
        time.sleep(2);
        return;

    @pytest.mark.release
    def test_MealApp_Auth(self):
        step.log_into_Staging(self.driver);
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/01Dashboard.png');
        step.go_to_meal_application_page(self.driver, '_Smoke Test Staging');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/02MealAppDistrict.png');
        step.click_by_xpath(self.driver, '//*[@id="null"]/linq-table-header/header/div[2]/linq-buttons/div/button');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/03MealAppPopUp.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/04MealAppStart.png');
        step.click_on(self.driver, 'generalInfoNext');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/05MealAppQuestions.png');
        step.click_on(self.driver, 'additionalQuestionsFormNext')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/06MealAppLetter.png');
        step.click_on(self.driver, 'letterToHouseholdNext')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/07Student.png');
        step.click_by_xpath(self.driver, '//*[@id="null"]/div[2]/div/button');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/08NewStudent.png');
        step.insert_text_by_id(self.driver, 'firstNameStudentForm', 'Brian');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/09SetFName.png');
        step.insert_text_by_id(self.driver, 'lastNameStudentForm', 'Student');
        step.click_on(self.driver, 'dateOfBirthStudentForm');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/10SetLName.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/11StudentAdded.png');
        step.insert_text_by_id(self.driver, 'studentIncome', '1000')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/12StudentIncome.png');
        # time.sleep(5);
        step.click_on(self.driver, 'studentsNext');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/13Household.png');
        step.insert_text_by_id(self.driver, 'numberOfHouseholdMembers', '2');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/14NumOfHouseholdSet.png');
        step.click_on(self.driver, 'newAdult');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/15AddMember.png');
        step.insert_text_by_id(self.driver, 'firstName', 'Brian');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/16SetFName.png');
        step.insert_text_by_id(self.driver, 'lastName', 'Test');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/17SetLName.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/18Confirm.png');
        step.click_on(self.driver, 'householdNext');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/19Review1.png');
        step.scroll_to_by_id(self.driver, 'editHousehold')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/19Review2.png');
        step.scroll_to_by_id(self.driver, 'reviewNext');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/20Review3.png');
        step.click_on(self.driver, 'reviewNext');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/20Submit1.png');
        step.insert_text_by_id(self.driver, 'signedBy', 'Brian Burningham');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/21Submit2.png');
        step.click_on(self.driver, 'noSSN');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/22Submit3.png');
        step.insert_text_by_id(self.driver, 'signedBy', 'Brian Test');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/23Submit4.png');
        step.scroll_to_by_id(self.driver, 'submit');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/24Submit5.png');
        step.click_on(self.driver, 'submit');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/25Submit6.png');
        step.click_on(self.driver, 'dialog-confirm');
        return;

    @pytest.mark.release
    def test_MealApp_DistrictWithAssistance(self):
        step.log_into_Staging(self.driver);
        step.go_to_meal_application_page(self.driver, '_Smoke Test Staging');
        step.click_by_xpath(self.driver, '//*[@id="null"]/linq-table-header/header/div[2]/linq-buttons/div/button');
        step.click_on(self.driver, 'dialog-confirm');
        step.click_on(self.driver, 'generalInfoNext');
        step.click_on(self.driver, 'additionalQuestionsFormNext');
        step.click_on(self.driver, 'letterToHouseholdNext');
        step.click_by_xpath(self.driver, '//*[@id="null"]/linq-table-header/header/div[2]/linq-buttons/div/button');
        step.insert_text_by_id(self.driver, 'firstNameStudentForm', 'Brian');
        step.insert_text_by_id(self.driver, 'lastNameStudentForm', 'Burningham');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.click_on(self.driver, 'studentsNext');
        step.insert_text_by_id(self.driver, 'numberOfHouseholdMembers', '2');
        #step.wait_until_not_displayed(self.driver, 'cdk-overlay-pane');
        step.click_on(self.driver, 'newAdult')
        step.insert_text_by_id(self.driver, 'firstName', 'Brian');
        step.insert_text_by_id(self.driver, 'lastName', 'Test');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.click_on(self.driver, 'householdNext');
        step.click_on(self.driver, 'reviewPrevious');
        step.click_on(self.driver, 'householdNextPrevious')
        step.click_on(self.driver, 'studentsPrevious');
        step.click_on(self.driver, 'letterToHouseholdPrevious');
        step.click_on(self.driver, 'additionalQuestionsFormPrevious');
        step.click_on(self.driver, 'eligibilityBenefitType');
        step.click_on(self.driver, 'Food Distribution Program on Indian... (FDPIR)');
        step.insert_text_by_id(self.driver, 'caseNumber', '123');
        step.click_on(self.driver, 'generalInfoNext');
        step.click_on(self.driver, 'additionalQuestionsFormNext');
        step.click_on(self.driver, 'letterToHouseholdNext');
        step.click_on(self.driver, 'studentsNext');
        step.click_on(self.driver, 'reviewPrevious');
        #step.click_on(self.driver, 'householdNextPrevious')
        step.click_on(self.driver, 'studentsPrevious');
        step.click_on(self.driver, 'letterToHouseholdPrevious');
        step.click_on(self.driver, 'additionalQuestionsFormPrevious');
        step.click_on(self.driver, 'eligibilityBenefitType');
        step.click_on(self.driver, 'assistanceBlankValue');
        step.click_on(self.driver, 'generalInfoNext');
        step.click_on(self.driver, 'additionalQuestionsFormNext');
        step.click_on(self.driver, 'letterToHouseholdNext');
        step.click_on(self.driver, 'studentsNext');
        step.scroll_to_by_id(self.driver, 'householdNext');
        step.take_screenshot(self.driver, 'Release/MealApp/DistrictsWithAssistance/01NextNotActive.png');
        step.insert_text_by_id(self.driver, 'numberOfHouseholdMembers', '2');
        step.take_screenshot(self.driver, 'Release/MealApp/DistrictsWithAssistance/02HouseholdNumRequired.png');
        step.click_on(self.driver, 'householdNext');
        step.click_on(self.driver, 'reviewPrevious');
        step.click_on(self.driver, 'householdNextPrevious')
        step.click_on(self.driver, 'studentsPrevious');
        step.click_on(self.driver, 'letterToHouseholdPrevious');
        step.click_on(self.driver, 'additionalQuestionsFormPrevious');
        step.click_on(self.driver, 'eligibilityBenefitType');
        step.click_on(self.driver, 'Supplemental Nutrition Assistance Program (SNAP)');
        step.insert_text_by_id(self.driver, 'caseNumber', '123');
        step.click_on(self.driver, 'generalInfoNext');
        step.click_on(self.driver, 'additionalQuestionsFormNext');
        step.click_on(self.driver, 'letterToHouseholdNext');
        step.click_on(self.driver, 'studentsNext');
        step.click_on(self.driver, 'reviewPrevious');
        #step.click_on(self.driver, 'householdNextPrevious')
        step.click_on(self.driver, 'studentsPrevious');
        step.click_on(self.driver, 'letterToHouseholdPrevious');
        step.click_on(self.driver, 'additionalQuestionsFormPrevious');
        step.click_on(self.driver, 'eligibilityBenefitType');
        step.click_on(self.driver, 'assistanceBlankValue');
        step.click_on(self.driver, 'generalInfoNext');
        step.click_on(self.driver, 'additionalQuestionsFormNext');
        step.click_on(self.driver, 'letterToHouseholdNext');
        step.click_on(self.driver, 'studentsNext');
        step.scroll_to_by_id(self.driver, 'householdNext');
        step.take_screenshot(self.driver, 'Release/MealApp/DistrictsWithAssistance/03NextNotActive.png');
        step.insert_text_by_id(self.driver, 'numberOfHouseholdMembers', '2');
        step.take_screenshot(self.driver, 'Release/MealApp/DistrictsWithAssistance/04HouseholdNumRequired.png');
        step.click_on(self.driver, 'householdNext');
        step.take_screenshot(self.driver, 'Release/MealApp/DistrictsWithAssistance/05Review.png');
        return;

    @pytest.mark.release_wip
    def Store_(self):
        step.log_into_Staging(self.driver);
        step.go_to_store(self.driver, '_Smoke Test Staging');
        step.click_on(self.driver, 'item-online-store-eligibility-item');
        step.click_on(self.driver, 'student');
        #Blocked until id's are added for student dropdown and Unit Drop down
        return;

    @pytest.mark.release
    def test_Home_UpdateStudent_Enrolled(self):
        When.log_into_Staging(self.driver);
        And.log_into_district_portal(self.driver);
        And.update_student_info(self.driver, '5252', '102111', lastName='Potter2');
        step.take_screenshot(self.driver, 'Release/Home/UpdateStudentEnrolled/01LastNameUpdate.png');
        And.switch_tab(self.driver, 0);
        And.refresh_the_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/UpdateStudentEnrolled/02LCLastNameUpdate.png');
        #time.sleep(5);
        And.switch_tab(self.driver, 1);
        And.update_student_info(self.driver, '5252', '102111', lastName='Potter');
        step.take_screenshot(self.driver, 'Release/Home/UpdateStudentEnrolled/03LastNamerevert.png');
        And.switch_tab(self.driver, 0);
        And.refresh_the_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/UpdateStudentEnrolled/04LCLastNamerevert.png');
        return;

    @pytest.mark.release
    def test_Home_UpdateStudent_NotEnrolled(self):
        When.log_into_Staging(self.driver);
        And.log_into_district_portal(self.driver);
        And.update_student_info(self.driver, '5252', '6820', lastName='ABRAMS2');
        step.take_screenshot(self.driver, 'Release/Home/UpdateStudentNotEnrolled/01LastNameUpdate.png');
        And.switch_tab(self.driver, 0);
        And.refresh_the_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/UpdateStudentNotEnrolled/02LCLastNameUpdate.png');
        # time.sleep(5);
        And.switch_tab(self.driver, 1);
        And.update_student_info(self.driver, '5252', '6820', lastName='ABRAMS');
        step.take_screenshot(self.driver, 'Release/Home/UpdateStudentNotEnrolled/03LastNamerevert.png');
        And.switch_tab(self.driver, 0);
        And.refresh_the_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/UpdateStudentNotEnrolled/04LCLastNamerevert.png');
        return;

    @pytest.mark.release
    def test_Home_UpdateStaff(self):
        When.log_into_Staging(self.driver);
        And.log_into_district_portal(self.driver);
        And.update_staff_info(self.driver, '0011', '432112', lastName='Staff 3 - test');
        step.take_screenshot(self.driver, 'Release/Home/UpdateStaff/01StaffLastNameUpdate.png');
        And.switch_tab(self.driver, 0);
        And.refresh_the_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/UpdateStaff/02LCStaffLastNameUpdate.png');
        And.switch_tab(self.driver, 1);
        And.update_staff_info(self.driver, '0011', '432112', lastName='Staff 3');
        step.take_screenshot(self.driver, 'Release/Home/UpdateStaff/01StaffLastNameRevert.png');
        And.switch_tab(self.driver, 0);
        And.refresh_the_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/UpdateStaff/04LCStaffLastNameRevert.png')
        return;

    @pytest.mark.release
    def test_Announcement_Widget(self):
        When.log_into_Staging(self.driver);
        And.log_into_district_portal(self.driver);
        And.create_new_announcement(self.driver, '0011');
        And.go_to_district_dashboard(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/AnnouncementWidget/01DistrictDashboard.png')
        And.switch_tab(self.driver, 0);
        And.refresh_the_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/AnnouncementWidget/02LCDashboard.png')
        And.switch_tab(self.driver, 1);
        And.update_announcement(self.driver, '0011', endDate=step.yesterday());
        And.go_to_district_dashboard(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/AnnouncementWidget/03DistrictDashboard.png')
        And.switch_tab(self.driver, 0);
        And.refresh_the_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/AnnouncementWidget/04LCDashboard.png')
        return;

if __name__ == '__main__':
    unittest.main()
