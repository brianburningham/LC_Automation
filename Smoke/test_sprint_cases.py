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
import sprint_steps as ss_step, sprint_steps as ss_When, sprint_steps as ss_And, sprint_steps as ss_Then

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

class MyTestCase(base.testFixture):
    @pytest.mark.sprint1107
    def test_TransactionHistory_FullDescription(self):
        When.log_into_Staging(self.driver);
        And.go_to_history(self.driver);
        Then.should_see_text(self.driver, 'Transaction');
        And.should_see_text(self.driver, 'Date');
        And.should_see_text(self.driver, 'Member Name');
        And.should_see_text(self.driver, 'Item');
        And.should_see_text(self.driver, 'Total');
        And.should_see_text(self.driver, 'Ending Balance');
        And.should_see_text(self.driver, 'Status');
        And.should_not_see_text(self.driver, 'help me');
        return;

    @pytest.mark.sprint1107
    # bug 191299 and 191287
    def test_TOS_AriaLabel(self):
        When.log_into_Staging(self.driver);
        And.go_to_account_page(self.driver);
        ss_And.add_new_autopay_sprint1107(self.driver, district='autoPay - TITAN Unified School District',
                                          student='autoPay - Harry Potter',
                                          addAmount='10', belowAmount='150');
        Then.should_see_element(self.driver, css_selector="[aria-label='Close']");
        And.click_on(self.driver, 'autoPayTermsOfService');
        Then.should_see_element(self.driver, css_selector="[aria-label='Close']");
        return;

    @pytest.mark.sprint1121
    def test_link_staff_with_DOB(self):
        When.log_into_district_portal(self.driver);
        And.select_district(self.driver, '5252');
        And.go_to_district_management(self.driver);
        And.go_to_LINQConnect_tab(self.driver);
        And.enable_link_staff_by_DOB(self.driver);
        And.switch_tab(self.driver, 0);
        When.log_into_Staging(self.driver);
        And.link_staff(self.driver, 'TITAN Unified School District', 'sys-17', firstName='Kelley', lastName='Huston', DOB='05/05/1993');
        Then.should_see_text(self.driver, 'Kelley Huston');
        And.remove_linked_staff(self.driver, 'Kelley Huston');
        Then.should_not_see_text(self.driver, 'Kelley Huston');
        And.switch_tab(self.driver, 1);
        Then.disable_link_staff_by_DOB(self.driver);
        return;

    def test_menu_lines(self):
        When.insert_text_by_id(self.driver, 'districtSelectMenu', '0011');
        And.click_on(self.driver, 'cdk-overlay-0');
        And.click_by_xpath(self.driver, '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/titan-public-menu/titan-family-menu/div/div/div/div[3]/div[1]/div[3]/button[1]/span[1]/mat-icon');
        And.click_on(self.driver, 'servingLine');
        time.sleep(2);
        parent = self.driver.find_element(By.ID, 'servingLine');
        all_children = parent.find_elements(By.XPATH, ".//input[@id]");
        for i in all_children:
            print(i.get_attribute('id'));
        return;

    def test_Added_Timezones(self):
        When.log_into_Staging(self.driver);
        And.go_to_profile(self.driver);
        And.click_on(self.driver, 'timeZoneId');
        for i in timezones:
            Then.should_see_text(self.driver, i);
            print(i);



if __name__ == '__main__':
    unittest.main()
