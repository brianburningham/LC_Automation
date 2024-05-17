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
    newmealappbutton = '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/ng-component/div/div[2]/div/div/div/div/titan-card/mat-card/mat-card-content/div/linq-connect-table/linq-table/div/linq-table-header/header/div[2]/linq-buttons/div/button'
    addstudentbutton = '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/titan-meal-application/div/div/div/div[2]/mat-card/mat-card-content/form/div[1]/mat-horizontal-stepper/div/div[2]/div[4]/titan-meal-application-students/students-table/linq-connect-table/linq-table/div/linq-table-header/header/div[2]/linq-buttons/div/button'
    guestaddstudent = '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/titan-public-meal-application/titan-meal-application/div/div/div/div[2]/mat-card/mat-card-content/form/div[1]/mat-horizontal-stepper/div/div[2]/div[4]/titan-meal-application-students/students-table/linq-connect-table/linq-table/div/linq-table-header/header/div[2]/linq-buttons/div/button'

    @pytest.mark.release
    def test_MealApp_Eng_noAuth(self):
        When.click_on(self.driver, 'headerSchoolServices');
        And.click_on(self.driver, 'headerSchoolServices-MealApplication');
        And.insert_text_by_id(self.driver, 'districtSingleSelect', '_Smoke Test Staging');
        time.sleep(2);
        And.click_on(self.driver, 'cdk-overlay-0');
        step.click_on(self.driver, 'loadSelectedDistrict');
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/01MealApp_eng_GeneralInfo.png');
        step.click_on(self.driver, 'generalInfoNext')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Eng/02MealApp_eng_AdditionalQuestions.png');
        step.click_on(self.driver, 'additionalQuestionsFormNext')
        step.take_screenshot(self.driver,
                             'Release/MealApp/MealApp_noAuth/Eng/03MealApp_eng_Letter.png');
        step.click_on(self.driver, 'letterToHouseholdNext')
        step.click_by_aria_label(self.driver, 'Add Students');
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
        step.insert_text_by_id(self.driver, 'firstNameHouseholdForm', 'Brian');
        step.insert_text_by_id(self.driver, 'lastNameHouseholdForm', 'Burningham');
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
        When.click_on(self.driver, 'headerSchoolServices');
        And.click_on(self.driver, 'headerSchoolServices-MealApplication');
        And.click_on(self.driver, 'global-header-hamburger-button');
        step.set_language_to(self.driver, 'Spanish');
        And.click_on(self.driver, 'global-header-hamburger-button');
        step.insert_text_by_id(self.driver, 'districtSingleSelect', '_Smoke Test Staging');
        time.sleep(2);
        And.click_on(self.driver, 'cdk-overlay-1');
        step.click_on(self.driver, 'loadSelectedDistrict');
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/01MealApp_spa_GeneralInfo.png');
        step.click_on(self.driver, 'generalInfoNext')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_noAuth/Spa/02MealApp_spa_AdditionalQuestions.png');
        step.click_on(self.driver, 'additionalQuestionsFormNext')
        step.take_screenshot(self.driver,
                             'Release/MealApp/MealApp_noAuth/Spa/03MealApp_eng_Letter.png');
        step.click_on(self.driver, 'letterToHouseholdNext')
        step.click_by_aria_label(self.driver, 'Agregar estudiantes');
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
        step.insert_text_by_id(self.driver, 'firstNameHouseholdForm', 'Brian');
        step.insert_text_by_id(self.driver, 'lastNameHouseholdForm', 'Burningham');
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

    @pytest.mark.release_wip
    def test_MealApp_Auth(self):
        step.log_into_Staging(self.driver);
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/01Dashboard.png');
        step.go_to_meal_application_page(self.driver, '_Smoke Test Staging');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/02MealAppDistrict.png');
        step.click_by_aria_label(self.driver, 'New Application');
        #step.click_by_xpath(self.driver, self.newmealappbutton);
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/03MealAppPopUp.png');
        step.click_on(self.driver, 'loadSelectedDistrict');
        step.click_on(self.driver, 'dialog-confirm');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/04MealAppStart.png');
        step.click_on(self.driver, 'generalInfoNext');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/05MealAppQuestions.png');
        step.click_on(self.driver, 'additionalQuestionsFormNext')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/06MealAppLetter.png');
        step.click_on(self.driver, 'letterToHouseholdNext')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/07Student.png');
        step.click_by_aria_label(self.driver, 'Add Students');
        #step.click_by_xpath(self.driver, self.addstudentbutton);
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
        step.insert_text_by_id(self.driver, 'firstNameHouseholdForm', 'Brian');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/16SetFName.png');
        step.insert_text_by_id(self.driver, 'lastNameHouseholdForm', 'Test');
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
        step.click_on(self.driver, 'noSSN-input');
        #step.click_by_xpath(self.driver, '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/titan-meal-application/div/div/div/div[2]/mat-card/mat-card-content/form/div[1]/mat-horizontal-stepper/div/div[2]/div[7]/titan-meal-application-submit/div[1]/div[3]/div[2]/div[2]/mat-checkbox')
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/22Submit3.png');
        step.insert_text_by_id(self.driver, 'signedBy', 'Brian Test');
        step.take_screenshot(self.driver, 'Release/MealApp/MealApp_Auth/23Submit4.png');
        #step.click_on(self.driver, 'noSSN');
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
        step.click_by_aria_label(self.driver, 'New Application');
        step.click_on(self.driver, 'loadSelectedDistrict');
        step.click_on(self.driver, 'dialog-confirm');
        step.click_on(self.driver, 'generalInfoNext');
        step.click_on(self.driver, 'additionalQuestionsFormNext');
        step.click_on(self.driver, 'letterToHouseholdNext');
        step.click_by_aria_label(self.driver, 'Add Students');
        step.insert_text_by_id(self.driver, 'firstNameStudentForm', 'Brian');
        step.insert_text_by_id(self.driver, 'lastNameStudentForm', 'Burningham');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.click_on(self.driver, 'studentsNext');
        step.insert_text_by_id(self.driver, 'numberOfHouseholdMembers', '2');
        # step.wait_until_not_displayed(self.driver, 'cdk-overlay-pane');
        step.click_on(self.driver, 'newAdult')
        step.insert_text_by_id(self.driver, 'firstNameHouseholdForm', 'Brian');
        step.insert_text_by_id(self.driver, 'lastNameHouseholdForm', 'Test');
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
        # step.click_on(self.driver, 'householdNextPrevious')
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
        # step.click_on(self.driver, 'householdNextPrevious')
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

if __name__ == '__main__':
    unittest.main()