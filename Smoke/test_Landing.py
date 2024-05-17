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
    def test_Landing_Text(self):
        When.should_see_text(self.driver, 'No more scrambling for cash. Give your students instant access to funds.');
        And.should_see_text(self.driver, 'With LINQ Connect, you can manage school-related fees and meal balances in one place. Make secure payments from anywhere you have internet access. Feel good knowing your kids have lunch money when they need it.')
        And.should_see_text(self.driver, 'Simplify Life with LINQ Connect')
        And.should_see_text(self.driver, 'Securely send money to school anytime, anywhere.')
        And.should_see_text(self.driver, 'Safely access your LINQ Connect account through our app or online and find all the features you need including automatic payments, low balance notifications and detailed reports.')
        And.should_see_text(self.driver, 'Manage all of your students in one place.')
        And.should_see_text(self.driver, 'One dashboard to view all the district students in your household provides an easy way to reload funds and transfer money between them.')
        And.should_see_text(self.driver, 'Get real-time information about purchases made.')
        And.should_see_text(self.driver, 'No need to endure the wait for end-of-day information uploads. Experience the convenience of receiving updates on your balances and transactions as they happen, in real-time.')
        And.should_see_text(self.driver, 'More than just a place to make payments, LINQ Connect is designed to make your life easier. ')
        And.should_see_text(self.driver, 'Maximize the benefits of LINQ Connect this school year.')
        And.should_see_text(self.driver, 'Access and store important forms such as meal applications and permission slips.')
        And.should_see_text(self.driver, 'Set up reminders and balance notifications.')
        And.should_see_text(self.driver, 'View nutritional and allergen information of school menu items.')
        And.should_see_text(self.driver, 'Make one-time payments or schedule automatic payments to meet your needs')
        And.should_see_text(self.driver, 'Pay fees and make school-related purchases.')
        And.should_see_text(self.driver, 'Budget funds with daily spending limit capabilities.')
        And.should_see_text(self.driver, 'Make donations anytime to help your school.')
        And.should_see_text(self.driver, 'Some features not available in all schools.')
        And.should_see_text(self.driver, "It's as easy as 1, 2, 3!")
        And.should_see_text(self.driver, 'More than one million families already use LINQ Connect. Get started today.')
        And.should_see_text(self.driver, 'Ready, Set, Payments: A Comprehensive Family Back-to-School Payments Checklist')
        And.should_see_text(self.driver, 'Make Student Payments Easier with a Single App: LINQ Connect')
        And.should_see_text(self.driver, 'Parent Tips for Managing K-12 Payments')
        And.should_see_text(self.driver, 'Parent Resources')
        And.should_see_text(self.driver, 'Useful resources are at your fingertips. Visit the resource page for a library full of instructional videos and blogs written by parents, just like you.')
        And.should_see_text(self.driver, "Whether you need to pay for that field trip or load your student's account for meal payments, LINQ Connect has everything you need. Get started today.")
        And.should_see_text(self.driver, 'Join LINQ Connect')
        And.should_see_text(self.driver, 'Frequently Asked Questions')
        And.should_see_text(self.driver, 'Still have questions? Visit our Frequently Asked Questions to learn about everything LINQ Connect has to offer.')
        And.should_see_text(self.driver, 'View Frequently Asked Questions')
        And.should_see_text(self.driver, 'LINQ empowers the business of K-12 schools.')
        And.should_see_text(self.driver, '2528 Independence Blvd. ')
        And.should_see_text(self.driver, 'Wilmington, NC 28412')
        And.should_see_text(self.driver, '844.467.4700')
        And.should_see_text(self.driver, 'support@linqconnect.com')
        And.should_see_text(self.driver, '©')
        And.should_see_text(self.driver, 'Privacy Policy')
        And.should_see_text(self.driver, 'Terms of Service')
        And.should_see_text(self.driver, 'EMS LINQ, LLC. All rights reserved')
        return;

    @pytest.mark.release
    def test_SchoolMenu_DistrictSearch(self):
        When.go_to_school_menu_as_guest(self.driver);
        And.insert_text_by_id(self.driver, 'districtSelectMenu' ,'0013');
        And.click_on(self.driver, 'districtSelectorOption-_FederalWay');
        And.click_on(self.driver, '0-district-selector-next');
        Then.should_see_text(self.driver, 'Sorry, but this district does not have a menu published online.');
        When.insert_text_by_id(self.driver, 'districtSelectMenu', '0011');
        And.click_on(self.driver, 'districtSelectorOption-_SmokeTestStaging');
        And.click_on(self.driver, '0-district-selector-next');
        time.sleep(5)
        Then.should_see_text(self.driver, 'Monday');
        Then.should_see_text(self.driver, 'Tuesday');
        Then.should_see_text(self.driver, 'Wednesday');
        Then.should_see_text(self.driver, 'Thursday');
        Then.should_see_text(self.driver, 'Friday');
        Then.log_result("Menu Plans - District Search part 1 - Pass");
        return;

    @pytest.mark.release
    def test_SchoolMenu_DistrictSearch_CancelButton(self):
        When.go_to_school_menu_as_guest(self.driver);
        And.insert_text_by_id(self.driver, 'districtSelectMenu', '0013');
        And.click_on(self.driver, 'districtSelectorOption-_FederalWay');
        And.click_on(self.driver, '0-district-selector-next');
        Then.should_see_text(self.driver, 'Sorry, but this district does not have a menu published online.');
        When.click_on(self.driver, '0-district-selector-cancel');
        Then.should_not_see_text(self.driver, 'Sorry, but this district does not have a menu published online.');
        Then.log_result("Menu Plans - District Search part 2 - Pass");
        return;

    @pytest.mark.release
    def test_SchoolMenu_LINQConnectLink(self):
        When.go_to_school_menu_as_guest(self.driver);
        And.insert_text_by_id(self.driver, 'districtSelectMenu', '0011');
        And.click_on(self.driver, 'districtSelectorOption-_SmokeTestStaging');
        And.click_on(self.driver, '0-district-selector-next');
        time.sleep(5);
        And.should_see_text(self.driver, 'Monday');
        And.should_see_text(self.driver, 'Tuesday');
        And.should_see_text(self.driver, 'Wednesday');
        And.should_see_text(self.driver, 'Thursday');
        And.should_see_text(self.driver, 'Friday');
        And.click_on(self.driver, 'global-header-product-button');
        And.should_see_text(self.driver, 'With LINQ Connect,');
        Then.log_result("Menu Plans - LINQ Connect link - Pass");
        return;

    @pytest.mark.release
    def test_SchoolMenu_Register(self):
        When.go_to_school_menu_as_guest(self.driver);
        And.insert_text_by_id(self.driver, 'districtSelectMenu', '0011');
        And.click_on(self.driver, 'districtSelectorOption-_SmokeTestStaging');
        And.click_on(self.driver, '0-district-selector-next');
        And.click_on(self.driver, 'global-header-profile-button');
        And.click_on(self.driver, 'landingPageRegisterButton');
        Then.should_see_text(self.driver, 'Please complete fields to register a new account in LINQ Connect. Required fields are marked with *.');
        Then.log_result("Menu Plans - Register button - Pass");
        return;

    @pytest.mark.release
    def test_SchoolMenu_Login(self):
        When.go_to_school_menu_as_guest(self.driver);
        And.insert_text_by_id(self.driver, 'districtSelectMenu', '0011');
        And.click_on(self.driver, 'districtSelectorOption-_SmokeTestStaging');
        And.click_on(self.driver, '0-district-selector-next');
        And.click_on(self.driver, 'global-header-profile-button');
        And.click_on(self.driver, 'landingPageLoginButton');
        Then.should_see_text(self.driver,'Sign in to LINQ Connect');
        Then.log_result("Menu Plans - Login button - Pass");
        return;

    @pytest.mark.release
    def test_SchoolMenu_Languages(self):
        When.go_to_school_menu_as_guest(self.driver);
        And.insert_text_by_id(self.driver, 'districtSelectMenu', '0011');
        And.click_on(self.driver, 'districtSelectorOption-_SmokeTestStaging');
        And.click_on(self.driver, '0-district-selector-next');
        #Spanish
        And.click_on(self.driver, 'global-header-hamburger-button');
        And.set_language_to(self.driver, 'Spanish');
        And.click_on(self.driver, 'global-header-hamburger-button');
        Then.should_see_text(self.driver, 'miércoles');
        #Armenian
        And.click_on(self.driver, 'global-header-hamburger-button');
        And.set_language_to(self.driver, 'Armenian');
        And.click_on(self.driver, 'global-header-hamburger-button');
        Then.should_see_text(self.driver, 'չորեքշաբթի');
        #Burmese
        And.click_on(self.driver, 'global-header-hamburger-button');
        And.set_language_to(self.driver, 'Burmese');
        time.sleep(5)
        And.click_on(self.driver, 'global-header-hamburger-button');
        Then.should_see_text(self.driver, 'ဗုဒ္ဓဟူး');
        #Chinese
        And.click_on(self.driver, 'global-header-hamburger-button');
        And.set_language_to(self.driver, 'Chinese');
        And.click_on(self.driver, 'global-header-hamburger-button');
        Then.should_see_text(self.driver, '星期三');
        #French
        And.click_on(self.driver, 'global-header-hamburger-button');
        And.set_language_to(self.driver, 'French');
        And.click_on(self.driver, 'global-header-hamburger-button');
        Then.should_see_text(self.driver, 'mercredi');
        #Korean
        And.click_on(self.driver, 'global-header-hamburger-button');
        And.set_language_to(self.driver, 'Korean');
        And.click_on(self.driver, 'global-header-hamburger-button');
        Then.should_see_text(self.driver, '수요일');
        #Portuguese
        And.click_on(self.driver, 'global-header-hamburger-button');
        And.set_language_to(self.driver, 'Portuguese');
        And.click_on(self.driver, 'global-header-hamburger-button');
        Then.should_see_text(self.driver, 'quarta-feira');
        #Russian
        And.click_on(self.driver, 'global-header-hamburger-button');
        And.set_language_to(self.driver, 'Russian');
        And.click_on(self.driver, 'global-header-hamburger-button');
        Then.should_see_text(self.driver, 'Обед');
        #vietnamese
        And.click_on(self.driver, 'global-header-hamburger-button');
        And.set_language_to(self.driver, 'Vietnamese');
        And.click_on(self.driver, 'global-header-hamburger-button');
        Then.should_see_text(self.driver, 'Thứ Tư');
        Then.log_result("Menu Plans - Languages - Pass");
        return;

    @pytest.mark.release
    def test_SchoolStore_DistrictSelect(self):
        When.go_to_school_store_as_guest(self.driver);
        And.insert_text_by_id(self.driver, 'districtSelectMenu', '0013');
        And.click_on(self.driver, 'districtSelectorOption-_FederalWay');
        And.click_on(self.driver, '1-district-selector-next');
        Then.should_see_text(self.driver, 'Sorry, but this district does not have a store published online.');
        When.insert_text_by_id(self.driver, 'districtSelectMenu', '0011');
        And.click_on(self.driver, 'districtSelectorOption-_SmokeTestStaging');
        And.click_on(self.driver, '1-district-selector-next');
        time.sleep(8);
        Then.should_see_text(self.driver,'_Smoke Test Staging');
        Then.log_result("School Store - District Select - Pass");
        return;

    @pytest.mark.release
    def test_SchoolStore_Filters(self):
        When.go_to_school_store_as_guest(self.driver);
        And.insert_text_by_id(self.driver, 'districtSelectMenu', '0011');
        And.click_on(self.driver, 'districtSelectorOption-_SmokeTestStaging');
        And.click_on(self.driver, '1-district-selector-next');
        time.sleep(5)
        And.should_see_text(self.driver, '_Smoke Test Staging');
        And.click_on(self.driver, 'storeListFilter-categories');
        And.click_on(self.driver, 'category-category-1');
        And.should_see_text(self.driver, 'Apple Test');
        And.should_not_see_text(self.driver, 'Test Fee 2')
        And.click_on(self.driver, 'filterChipRemove-category-1');
        And.should_see_text(self.driver, 'Apple Test');
        And.should_see_text(self.driver, 'Test Fee 2')
        And.click_on(self.driver, 'category-school-fees');
        And.should_see_text(self.driver, 'Test Fee 2');
        And.should_not_see_text(self.driver, 'Apple Test');
        And.click_on(self.driver, 'filterChipRemove-school-fees');
        Then.should_see_text(self.driver, 'Test Fee 2');
        Then.should_see_text(self.driver, 'Apple Test');
        Then.should_see_text(self.driver, 'Online Store User Priced Item');
        Then.log_result('School Store - Filters - Pass')
        time.sleep(2)
        return;

    @pytest.mark.release
    def test_SchoolStore_Pagination(self):
        When.go_to_school_store_as_guest(self.driver);
        And.insert_text_by_id(self.driver, 'districtSelectMenu', '9013');
        And.click_on(self.driver, 'districtSelectorOption-TitanSchoolDistrict-DONOTRENAME');
        And.click_on(self.driver, '1-district-selector-next');
        time.sleep(5);
        And.should_see_text(self.driver, 'Titan School District - DO NOT RENAME');
        And.click_by_aria_label(self.driver, 'Items per page:');
        And.click_by_xpath(self.driver, '/html/body/div[2]/div[2]/div/div/div/mat-option[1]/span');
        time.sleep(5)
        Then.should_not_see_text(self.driver,'A merchant test - bad processor');
        time.sleep(5)
        When.click_by_aria_label(self.driver, 'Next page');
        time.sleep(5)
        Then.should_see_text(self.driver, 'A merchant test - bad processor');
        Then.log_result('School Store - Pagination - Pass')
        #time.sleep(2)
        return;

    @pytest.mark.release
    def test_SchoolStore_Search(self):
        When.go_to_school_store_as_guest(self.driver);
        And.insert_text_by_id(self.driver, 'districtSelectMenu', '9013');
        And.click_on(self.driver, 'districtSelectorOption-TitanSchoolDistrict-DONOTRENAME');
        And.click_on(self.driver, '1-district-selector-next');
        And.should_see_text(self.driver, 'Titan School District - DO NOT RENAME');
        And.insert_text_by_id(self.driver, 'searchBox', 'A merchant test - bad processor');
        Then.should_see_text(self.driver, 'A merchant test - bad processor');
        Then.should_not_see_text(self.driver, 'A merchant test - good processor');
        Then.log_result('School Store - Search');
        return;

    @pytest.mark.release
    def test_SchoolStore_GuestCheckOut(self):
        When.go_to_school_store_as_guest(self.driver);
        And.insert_text_by_id(self.driver, 'districtSelectMenu', '0011');
        And.click_on(self.driver, 'districtSelectorOption-_SmokeTestStaging');
        And.click_on(self.driver, '1-district-selector-next');
        #And.should_see_text(self.driver, '_Smoke Test Staging');
        And.click_on(self.driver, 'item-apple-test');
        And.should_see_text(self.driver, 'Delicious apple for testing purposes...');
        And.insert_text_by_id(self.driver, 'donation', '25');
        And.insert_text_by_id(self.driver, 'donationNote', 'Testing');
        And.click_on(self.driver, 'addToCart');
        And.should_see_text(self.driver, '$25.00 USD');
        And.click_on(self.driver, 'linqConnectSheetCloseSheetX');
        And.should_not_see_text(self.driver, '$25.00 USD');
        And.open_shopping_cart(self.driver);
        And.should_see_text(self.driver, '$25.00 USD');
        And.click_on(self.driver, 'linqConnectSheetCancelButton');
        And.should_not_see_text(self.driver, '$25.00 USD');
        And.open_shopping_cart(self.driver);
        And.go_to_checkout(self.driver);
        And.click_on(self.driver, 'paymentMethodCreditDebitCard');
        And.insert_text_by_id(self.driver, 'emailAddress', 'bburningham+automation@gmail.com');
        And.insert_text_by_id(self.driver, 'cardNumber', '4111111111111111');
        And.insert_text_by_id(self.driver, 'creditCartFirstName', 'Brian');
        And.insert_text_by_id(self.driver, 'creditCardLastName', 'Automation');
        And.click_on(self.driver, 'expirationMonth');
        And.click_by_xpath(self.driver, '/html/body/div[2]/div[2]/div/div/div/mat-option[1]');
        And.click_on(self.driver, 'expirationYear');
        And.click_by_xpath(self.driver, '/html/body/div[2]/div[2]/div/div/div/mat-option[2]');
        And.insert_text_by_id(self.driver, 'cvc', '123');
        And.insert_text_by_id(self.driver, 'firstName', 'Brian')
        And.insert_text_by_id(self.driver, 'lastName', 'Automation');
        And.insert_text_by_id(self.driver, 'address', '123 Automation St');
        And.insert_text_by_id(self.driver, 'city', 'Springville');
        And.click_on(self.driver, 'state');
        And.click_by_xpath(self.driver, '/html/body/div[2]/div[2]/div/div/div/mat-option[2]');
        And.insert_text_by_id(self.driver, 'zip', '12345');
        #And.confirm_and_pay(self.driver);
        And.click_on(self.driver, 'checkout-confirm-pay');
        time.sleep(8);
        Then.should_see_text(self.driver, 'Thank you for your order!');
        Then.log_result('Guest Checkout - Pass')
        #time.sleep(5);
        return;

    @pytest.mark.release
    def test_FAQ_Sections(self):
        #I had to use custom script for scrolling to the id for this test because it broke for all other tests if used
        obj = ['faqSchoolFees4', 'faqGettingStarted1', 'faqGettingStarted2', 'faqGettingStarted3', 'faqGettingStarted4', 'faqGettingStarted5', 'faqGettingStarted6',
        'faqMealPayments1', 'faqfaqMealPayments2', 'faqfaqMealPayments3', 'faqfaqMealPayments4', 'faqfaqMealPayments5', 'faqfaqMealPayments6', 'faqfaqMealPayments7',
        'faqfaqMealPayments8', 'faqfaqMealPayments9', 'faqfaqMealPayments10', 'faqfaqMealPayments11', 'faqSchoolFees1', 'faqSchoolFees2', 'faqSchoolFees3',
        'faqMealApplications1', 'faqMealApplications2', 'faqMealApplications3', 'faqSchoolMenus1', 'faqFeedItForward1', 'faqPaymentTypes1',
        'faqPaymentTypes2', 'faqPaymentTypes2', 'faqPaymentTypes3', 'faqPaymentTypes4', 'faqPaymentTypes5', 'faqPaymentTypes6', 'faqPaymentTypes7',
        'faqPaymentTypes8','faqPaymentTypes9', 'faqLinqConnectApp1', 'faqLinqConnectApp2', 'faqLinqConnectApp3', 'faqSecurity1', 'faqSecurity2',
        'faqSecurity3', 'faqSecurity4', 'faqSecurity5', 'faqSecurity6'];
        picnumber = 1;
        When.go_to_FAQ(self.driver);
        And.should_see_text(self.driver, 'Frequently Asked Questions');
        for i in obj:
            #print(i);
            And.take_screenshot(self.driver, 'Release/Landing/Sections/' + str(picnumber) + i + '.png');
            self.driver.execute_script(
                "arguments[0].scrollIntoView({'block':'center','inline':'center'})",
                self.driver.find_element(By.ID, i));
            time.sleep(1)
            self.driver.find_element(By.ID, i).click();
            picnumber += 1;
            And.take_screenshot(self.driver, 'Release/Landing/Sections/' + str(picnumber) + i + '.png');
            self.driver.execute_script(
                "arguments[0].scrollIntoView({'block':'center','inline':'center'})",
                self.driver.find_element(By.ID, i));
            time.sleep(1);
            self.driver.find_element(By.ID, i).click();
            picnumber += 1;
        Then.log_result('FAQ Sections - Pass (check images)');
        return;

    @pytest.mark.release
    def test_FAQ_JumpToSection(self):
        sections = ['#section-getting-started', '#section-meal-payments', '#section-school-fees',
                    '#section-meal-app', '#section-menus', '#section-feed-it-forward',
                    '#section-payment-types', '#section-app', '#section-security']
        picnumber = 1;
        When.go_to_FAQ(self.driver);
        for i in sections:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({'block':'center','inline':'center'})",
                self.driver.find_element(By.ID, 'scrollToElementSelector'));
            #And.take_screenshot(self.driver, 'Release/Landing/JumpToSections/' + str(picnumber) + i + '.png');
            time.sleep(1)
            section = self.driver.find_element(By.ID, 'scrollToElementSelector')
            drop=Select(section);
            drop.select_by_value(i);
            And.take_screenshot(self.driver, 'Release/Landing/JumpToSections/' + str(picnumber) + i + '.png');
            picnumber += 1;
            time.sleep(1);
        Then.log_result('FAQ Jump To Sections - Pass (check images)');
        return;

    def test_test(self):
        When.go_to_FAQ(self.driver);
        And.click_on(self.driver, 'faqSchoolFees4');
        time.sleep(1)
        And.click_on(self.driver, 'faqSchoolFees4');
        time.sleep(10)
        return

if __name__ == '__main__':
    unittest.main()
