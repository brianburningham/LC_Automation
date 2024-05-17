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

timezones = ('Cuba', 'Bolivia', 'West Greenland', 'Newfoundland', 'Casey', 'Davis', 'Dumont-d’Urville', 'Mawson',
             'Rothera', 'Syowa', 'Vostok', 'Anadyr', 'Indochina', 'Brunei Darussalam', 'Ulaanbaatar', 'East Timor',
             'Gulf', 'Tajikistan', 'Indochina', 'Hong Kong', 'Hovd', 'Irkutsk', 'Western Indonesia', 'Eastern Indonesia',
             'Petropavlovsk-Kamchatski', 'Nepal', 'Krasnoyarsk', 'Malaysia', 'Malaysia', 'Magadan', 'Central Indonesia',
             'Philippine', 'Gulf', 'Krasnoyarsk', 'Novosibirsk', 'Indochina', 'Western Indonesia', 'Korean', 'Sakhalin',
             'Uzbekistan', 'Korean', 'Uzbekistan', 'Ulaanbaatar', 'Indochina', 'Myanmar', 'Lord Howe', 'Samara',
             'Volgograd', 'Indian Ocean', 'Christmas Island', 'Cocos Islands', 'French Southern', 'Seychelles',
             'Maldives', 'Réunion', 'Apia', 'Chatham', 'Chuuk', 'Easter Island', 'Vanuatu', 'Tokelau',
             'Tuvalu', 'Galapagos', 'Gambier', 'Solomon Islands', 'Phoenix Islands', 'Line Islands', 'Kosrae',
             'Marshall Islands', 'Marquesas', 'Samoa', 'Nauru', 'Niue', 'Norfolk Island', 'New Caledonia', 'Palau',
             'Pitcairn', 'Ponape', 'Papua New Guinea', 'Cook Islands', 'Tahiti', 'Gilbert Islands', 'Wake Island',
             'Wallis', 'Futuna');

class MyTestCase(basetest.testFixture):
    @pytest.mark.testall
    def test_Added_Timezones(self):
        When.log_into_Test(self.driver);
        And.go_to_profile(self.driver);
        And.click_on(self.driver, 'timeZoneId');
        for i in timezones:
            Then.should_see_text(self.driver, i);
            print(i);
        return;

    def test_NewPaymentMethod_CC(self):
        When.log_into_Test(self.driver);
        And.go_to_profile(self.driver);
        And.click_on(self.driver, 'addPaymentMethod');
        And.click_on(self.driver, 'paymentMethodCreditDebitCard');
        And.insert_text_by_id(self.driver, 'paymentMethodDescription', 'Automation Payment');
        And.insert_text_by_id(self.driver, 'creditCartFirstName', 'Auto');
        And.insert_text_by_id(self.driver, 'creditCardLastName', 'Mation');
        And.insert_text_by_id(self.driver, 'cardNumber', '4111111111111111');
        And.click_on(self.driver, 'expirationMonth');
        And.click_by_xpath(self.driver, '//span[contains(text(),"2 - February")]')
        And.click_on(self.driver, 'expirationYear');
        And.click_by_xpath(self.driver, '//span[contains(text(),"2040")]')
        And.insert_text_by_id(self.driver, 'cvc', '123');
        And.insert_text_by_id(self.driver, 'firstName', 'Auto');
        And.insert_text_by_id(self.driver, 'lastName', 'Mation');
        And.insert_text_by_id(self.driver, 'address', '123 Cherry Tree Ln')
        And.insert_text_by_id(self.driver, 'city', 'Summerville');
        And.click_on(self.driver, 'state');
        And.click_by_xpath(self.driver, '//span[contains(text(),"Florida")]')
        And.insert_text_by_id(self.driver, 'zip', '12345')
        And.click_on(self.driver, 'linqConnectSheetConfirmButton');
        And.should_see_text(self.driver, 'Automation Payment')
        And.click_on(self.driver, 'deletePaymentMethod1')
        And.should_see_text(self.driver, 'Remove Payment Method');
        And.click_on(self.driver, 'dialog-cancel')
        And.should_see_text(self.driver, 'Automation Payment')
        And.click_on(self.driver, 'deletePaymentMethod1')
        And.should_see_text(self.driver, 'Remove Payment Method');
        And.click_on(self.driver, 'dialog-confirm')
        Then.should_not_see_text(self.driver, 'Automation Payment');
        #time.sleep(5);
        return;

    def test_NewPaymentMethod_ACH(self):
        When.log_into_Test(self.driver);
        And.go_to_profile(self.driver);
        And.click_on(self.driver, 'addPaymentMethod');
        And.click_on(self.driver, 'paymentMethodElectronicCheck');
        And.insert_text_by_id(self.driver, 'paymentMethodDescription', 'Automation ACH');
        And.click_on(self.driver, 'bankAccountType');

        time.sleep(5);
        return;

if __name__ == '__main__':
    unittest.main()
