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
    def test_Add_10_to_Balance_StudentCard(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/10/07_MealBalance_StartBalance.png');
        step.go_to_dashboard(self.driver);
        step.click_by_aria_label(self.driver, 'Add Meal Funds HarryPotter');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/10/01_MealBalance_OpenDropdown.png')
        step.click_on(self.driver, 'mealFundAddAmountOption-HarryPotter-10');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/10/02_MealBalance_Select10.png')
        step.click_by_xpath(self.driver, '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/main/ng-component/div/div/div/div[1]/div/div[1]/app-person-card/mat-card/mat-card-footer/div/button');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/10/03_MealBalance_AddToCart.png')
        step.open_shopping_cart(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/10/04_MealBalance_OpenCart.png')
        step.go_to_checkout(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/10/05_MealBalance_CheckOut.png')
        step.confirm_and_pay(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/10/06_MealBalance_Pay.png')
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/10/08_MealBalance_NewBalance.png')
        return;

    @pytest.mark.release
    def test_Add_20_to_Balance_StudentCard(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/20/07_MealBalance_StartBalance.png');
        step.go_to_dashboard(self.driver);
        step.click_by_aria_label(self.driver, 'Add Meal Funds HarryPotter');
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/20/01_MealBalance_OpenDropdown.png')
        step.click_on(self.driver, 'mealFundAddAmountOption-HarryPotter-20');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/20/02_MealBalance_Select10.png')
        step.click_by_xpath(self.driver,
                            '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/main/ng-component/div/div/div/div[1]/div/div[1]/app-person-card/mat-card/mat-card-footer/div/button');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/20/03_MealBalance_AddToCart.png')
        step.open_shopping_cart(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/20/04_MealBalance_OpenCart.png')
        step.go_to_checkout(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/20/05_MealBalance_CheckOut.png')
        step.confirm_and_pay(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/20/06_MealBalance_Pay.png')
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/20/08_MealBalance_NewBalance.png')
        return;

    @pytest.mark.release
    def test_Add_50_to_Balance_StudentCard(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/50/07_MealBalance_StartBalance.png');
        step.go_to_dashboard(self.driver);
        step.click_by_aria_label(self.driver, 'Add Meal Funds HarryPotter');
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/50/01_MealBalance_OpenDropdown.png')
        step.click_on(self.driver, 'mealFundAddAmountOption-HarryPotter-50');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/50/02_MealBalance_Select10.png')
        step.click_by_xpath(self.driver,
                            '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/main/ng-component/div/div/div/div[1]/div/div[1]/app-person-card/mat-card/mat-card-footer/div/button');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/50/03_MealBalance_AddToCart.png')
        step.open_shopping_cart(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/50/04_MealBalance_OpenCart.png')
        step.go_to_checkout(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/50/05_MealBalance_CheckOut.png')
        step.confirm_and_pay(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/50/06_MealBalance_Pay.png')
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/50/08_MealBalance_NewBalance.png')
        return;

    @pytest.mark.release
    def test_Add_Custom_to_Balance_StudentCard(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/Custom/07_MealBalance_StartBalance.png');
        step.go_to_dashboard(self.driver);
        step.click_by_aria_label(self.driver, 'Add Meal Funds HarryPotter');
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/Custom/01_MealBalance_OpenDropdown.png')
        step.insert_text_by_aria_label(self.driver, 'Add Meal Funds HarryPotter', '15')
        step.click_on(self.driver, 'HarryPotter-personCardChevronButton-expandLess');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/Custom/02_MealBalance_Custom.png')
        step.click_by_xpath(self.driver,
                            '/html/body/div[1]/titan-angular-root/ng-component/div/mat-sidenav-container/mat-sidenav-content/main/ng-component/div/div/div/div[1]/div/div[1]/app-person-card/mat-card/mat-card-footer/div/button');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMealBalanceCard/Custom/03_MealBalance_AddToCart.png')
        step.open_shopping_cart(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/Custom/04_MealBalance_OpenCart.png')
        step.go_to_checkout(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/Custom/05_MealBalance_CheckOut.png')
        step.confirm_and_pay(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/Custom/06_MealBalance_Pay.png')
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver,
                             'Release/Meal Balance/AddViaMealBalanceCard/Custom/08_MealBalance_NewBalance.png')
        return;
    @pytest.mark.release
    def test_Add_20_to_Balance_MenuNav(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/20/04Meal_Balance_20_start_amount.png');
        step.click_on(self.driver, 'option20-HarryPotter');
        step.click_on(self.driver, 'mealAccountBalanceAddButton');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/20/01Meal_Balance_20_Cart.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/20/02Meal_Balance_20_Checkout.png');
        step.wait_for(self.driver, 'checkout-confirm-pay');
        step.click_on(self.driver, 'checkout-confirm-pay');
        time.sleep(3)
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/20/03Meal_Balance_20_Complete1.png');
        time.sleep(3);
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/20/05Meal_Balance_20_new_amount.png');
        time.sleep(3);
        return;

    @pytest.mark.release
    def test_Add_50_to_Balance_MenuNav(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/50/01Meal_Balance_50_start_amount.png');
        step.click_on(self.driver, 'option50-HarryPotter');
        step.click_on(self.driver, 'mealAccountBalanceAddButton');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/50/02Meal_Balance_50_Cart.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/50/03Meal_Balance_50_Checkout.png');
        step.wait_for(self.driver, 'checkout-confirm-pay');
        step.click_on(self.driver, 'checkout-confirm-pay');
        time.sleep(3)
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/50/04Meal_Balance_50_Complete1.png');
        time.sleep(3);
        step.click_on(self.driver, 'global-header-product-button');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/50/04Meal_Balance_50_Complete2.png');
        time.sleep(3);
        return;

    @pytest.mark.release
    def test_Add_10_to_Balance_MenuNav(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/10/01Meal_Balance_10_start_amount.png');
        step.click_on(self.driver, 'option10-HarryPotter');
        step.click_on(self.driver, 'mealAccountBalanceAddButton');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/10/02Meal_Balance_10_Cart.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/10/03Meal_Balance_10_Checkout.png');
        step.wait_for(self.driver, 'checkout-confirm-pay');
        step.click_on(self.driver, 'checkout-confirm-pay');
        time.sleep(3)
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/10/04Meal_Balance_10_Complete1.png');
        time.sleep(3);
        step.click_on(self.driver, 'global-header-product-button');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/10/04Meal_Balance_10_Complete2.png');
        time.sleep(3);
        return;

    @pytest.mark.release
    def test_Add_Custom_to_Balance_MenuNav(self):
        step.log_into_Staging(self.driver);
        step.go_to_account_page(self.driver);
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/Custom/01Meal_Balance_Custom_start_amount.png');
        step.click_on(self.driver, 'otherButton-HarryPotter');
        step.insert_text_by_id(self.driver, 'mealAccountBalanceAmountInput-HarryPotter', '15');
        step.click_on(self.driver, 'mealAccountBalanceAddButton');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/Custom/02Meal_Balance_Custom_Cart.png');
        step.click_on(self.driver, 'linqConnectSheetConfirmButton');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/Custom/03Meal_Balance_Custom_Checkout.png');
        step.wait_for(self.driver, 'checkout-confirm-pay');
        step.click_on(self.driver, 'checkout-confirm-pay');
        time.sleep(3)
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/Custom/04Meal_Balance_Custom_Complete1.png');
        time.sleep(3);
        step.click_on(self.driver, 'global-header-product-button');
        step.take_screenshot(self.driver, 'Release/Meal Balance/AddViaMenuNav/Custom/04Meal_Balance_Custom_Complete2.png');
        time.sleep(3);
        return;


if __name__ == '__main__':
    unittest.main()