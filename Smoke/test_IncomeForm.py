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
    newincomeformbutton = '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/ng-component/div/div/div/div[2]/div/titan-card/mat-card/mat-card-content/div/linq-connect-table/linq-table/div/linq-table-header/header/div[2]/linq-buttons/div/button'
    @pytest.mark.release
    def test_IncomeForm_AddStudent(self):
        step.log_into_Staging(self.driver);
        step.go_to_income_form(self.driver);
        step.click_by_aria_label(self.driver, 'Add New Income Form');
        step.insert_text_by_id(self.driver, 'incomeFormGeneralFirstName', 'Brian');
        step.insert_text_by_id(self.driver, 'incomeFormGeneralLastName', 'Test');
        step.insert_text_by_id(self.driver, 'incomeFormPhone', '4355555555');
        step.click_on(self.driver, 'incomeFormGeneralNextButton');
        step.insert_text_by_id(self.driver, 'householdSize', '2');
        step.click_on(self.driver, 'newAdult');
        step.insert_text_by_id(self.driver, 'firstNameHouseholdForm', 'Brian');
        step.insert_text_by_id(self.driver, 'lastNameHouseholdForm', 'Test');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.click_on(self.driver, 'incomeFormHouseholdNextButton');
        step.click_by_aria_label(self.driver, 'Add Students');
        #step.click_by_xpath(self.driver, '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/titan-income-form/div/div/div/div[2]/mat-card/mat-card-content/form/div[1]/mat-horizontal-stepper/div/div[2]/div[3]/titan-family-forms-students/div[2]/students-table/linq-connect-table/linq-table/div/linq-table-header/header/div[2]/linq-buttons/div/button');
        step.insert_text_by_id(self.driver, 'firstNameStudentForm', 'Brian');
        step.insert_text_by_id(self.driver, 'lastNameStudentForm', 'Student');
        step.click_on(self.driver, 'dateOfBirthStudentForm');
        step.take_screenshot(self.driver, 'Release/IncomeForm/AddStudent/AddStudent_DatePlacement.png')
        time.sleep(2);
        return;


if __name__ == '__main__':
    unittest.main()
