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
    history_nextpage = '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/ng-component/div/div/div/div[2]/titan-card/mat-card/mat-card-content/div/linq-connect-table/linq-table/div/linq-table-footer/footer/div[2]/mat-paginator/div/div/div[2]/button[2]';

    @pytest.mark.release
    def test_History_FilterStudent(self):
        step.log_into_Staging(self.driver);
        step.go_to_history(self.driver);
        step.take_screenshot(self.driver, 'Release/History/FilterStudent/01History.png');
        step.click_by_xpath(self.driver,
                            '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/main/ng-component/div/div/div/div[2]/titan-card/mat-card/mat-card-content/div/linq-connect-table/linq-table/div/div[2]/ag-grid-angular/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/div/span');
        step.take_screenshot(self.driver, 'Release/History/FilterStudent/02Filter.png');
        step.click_by_xpath(self.driver, '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/main/ng-component/div/div/div/div[2]/titan-card/mat-card/mat-card-content/div/linq-connect-table/linq-table/div/div[2]/ag-grid-angular/div/div[6]/div/div[1]/span[2]');
        step.take_screenshot(self.driver, 'Release/History/FilterStudent/03Filter.png');
        step.insert_text_by_id(self.driver, 'ag-155-input', 'Harry Potter');
        step.take_screenshot(self.driver, 'Release/History/FilterStudent/04Student.png');
        self.driver.find_element(By.ID, 'ag-155-input').send_keys(Keys.ENTER);
        self.driver.find_element(By.ID, 'ag-155-input').send_keys(Keys.ESCAPE);
        step.take_screenshot(self.driver, 'Release/History/FilterStudent/05StudentFilter.png');
        step.click_by_class_name(self.driver, 'table-filter-chips__clear');
        #step.click_by_xpath(self.driver, '//*[@id="null"]/linq-table-filters/div/div/mat-chip')
        step.take_screenshot(self.driver, 'Release/History/FilterStudent/06FilterCleared.png');
        time.sleep(1);
        return;

    @pytest.mark.release
    def test_History_Pagination(self):
        step.log_into_Staging(self.driver);
        step.go_to_history(self.driver);
        step.take_screenshot(self.driver, 'Release/History/Pagination/01Page1.png');
        #step.click_by_xpath(self.driver, self.history_nextpage);
        step.click_by_aria_label(self.driver, 'Next page');
        step.take_screenshot(self.driver, 'Release/History/Pagination/02Page2.png');
        step.click_by_aria_label(self.driver, 'Next page');
        step.take_screenshot(self.driver, 'Release/History/Pagination/03Page3.png');
        step.click_by_aria_label(self.driver, 'Next page');
        step.take_screenshot(self.driver, 'Release/History/Pagination/04Page4.png')
        step.click_by_aria_label(self.driver, 'Next page');
        step.take_screenshot(self.driver, 'Release/History/Pagination/05Page5.png');
        step.click_by_aria_label(self.driver, 'Next page');
        step.take_screenshot(self.driver, 'Release/History/Pagination/06Page6.png');
        time.sleep(1);
        return;

    @pytest.mark.release_wip
    def test_History_Transaction(self):
        step.log_into_Staging(self.driver);
        step.go_to_history(self.driver);
        step.click_by_xpath(self.driver,
                            '//*[@id="null"]/div/ag-grid-angular/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[4]');
        step.take_screenshot(self.driver, 'Release/History/Transaction/01Transaction.png');
        return;

    @pytest.mark.release
    def test_History_Empty(self):
        step.click_on(self.driver, 'headerSignIn');
        step.log_in_with(self.driver, 'brian_smoke_test@gmail.com', 'Titan123!');
        step.go_to_history(self.driver);
        step.take_screenshot(self.driver, 'Release/History/Empty/01Empty.png');
        return;


if __name__ == '__main__':
    unittest.main()
