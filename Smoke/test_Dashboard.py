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
        step.click_on(self.driver, 'districtSelectorOption-TITANUnifiedSchoolDistrict');
        time.sleep(2);
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/05SlideOut.png');
        step.insert_text_by_id(self.driver, 'identifier', '1983');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/06SlideOut.png');
        step.insert_text_by_id(self.driver, 'firstName', 'Link');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/07SlideOut.png');
        step.insert_text_by_id(self.driver, 'lastName', 'Student');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/08SlideOut.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.click_on(self.driver, 'LinkStudent-personCardChevronButton-expandLess');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/09ExpandStudentCard.png');
        step.go_to_profile(self.driver);
        step.scroll_to_by_id(self.driver, 'profile-unlink-account-LinkStudent');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/10StudentListed.png');
        step.click_on(self.driver, 'profile-unlink-account-LinkStudent');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/11ConfirmUnlinkStudent.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStudentViaTopNav/12StudentRemoved.png');
        return;

    @pytest.mark.release
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
        step.click_on(self.driver, 'districtSelectorOption-TITANUnifiedSchoolDistrict');
        time.sleep(2);
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/05SlideOut.png');
        step.insert_text_by_id(self.driver, 'identifier', 'sys-1983');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/06SlideOut.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/07StaffAdded.png');
        step.go_to_profile(self.driver);
        step.scroll_to_by_id(self.driver, 'profile-unlink-account-LinkStaff');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/08StaffListed.png');
        step.click_on(self.driver, 'profile-unlink-account-LinkStaff');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/09ConfirmUnlinkStaff.png');
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Release/AddStudentStaff/AddStaffViaTopNav/10StaffRemoved.png');
        return;

    @pytest.mark.release
    def test_Home_TermsofUse(self):
        step.log_into_Staging(self.driver);
        step.click_on(self.driver, 'global-header-hamburger-button')
        step.click_on(self.driver, 'termsOfServiceButton');
        step.take_screenshot(self.driver, 'Release/Home/TermsofUse/01TermsofUse.png');
        step.click_by_xpath(self.driver, '//*[@id="dialog-close"]/span[1]/mat-icon');
        step.take_screenshot(self.driver, 'Release/Home/TermsofUse/02TermsofUseClosed.png');
        step.click_on(self.driver, 'termsOfServiceButton');
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
        step.should_see_text(self.driver, 'Dashboard');
        step.take_screenshot(self.driver, 'Release/Home/LINQLogo/03ReturntoDashboard.png');
        return;

    @pytest.mark.release
    def test_Home_UpdateStudent_Enrolled(self):
        When.log_into_Staging(self.driver);
        And.log_into_district_portal(self.driver);
        And.update_student_info(self.driver, '5252', '102111', lastName='Potter2');
        step.take_screenshot(self.driver, 'Release/Home/UpdateStudentEnrolled/01LastNameUpdate.png');
        And.switch_tab(self.driver, 0);
        And.refresh_the_page(self.driver);
        And.go_to_account_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Home/UpdateStudentEnrolled/02LCLastNameUpdate.png');
        # time.sleep(5);
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
        And.go_to_account_page(self.driver);
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
        And.go_to_account_page(self.driver);
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
