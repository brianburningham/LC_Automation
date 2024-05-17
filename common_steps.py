import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta
import os
import time
import base

def today():
    today = datetime.now();
    currentDate = today.strftime("%m/%d/%Y");
    return currentDate;

def twodaysago():
    twodaysago = datetime.now() - timedelta(days=2);
    twodaysagoDate = twodaysago.strftime("%m/%d/%Y");
    return twodaysagoDate;

def yesterday():
    yesterday = datetime.now() - timedelta(days=1);
    yesterdayDate = yesterday.strftime("%m/%d/%Y");
    return yesterdayDate;

def tomorrow():
    tomorrow = datetime.now() + timedelta(days=1);
    tomorrowdate = tomorrow.strftime("%m/%d/%Y")
    return tomorrowdate;

def log_in_with(driver, username, password):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))
        )
    finally:
        insert_text_by_id(driver, 'username', username);
        insert_text_by_id(driver, 'password', password);
        click_by_xpath(driver, '/html/body/main/section/div/div/div/form/div[2]/button');
        wait_for(driver, 'global-header-hamburger-button');
        return;

def log_into_Staging(driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'headerSignIn'))
        )
    finally:
        with open("C:\LC\Staginglogin.txt", "r") as text_file:
            data = text_file.readlines();
        click_on(driver, 'headerSignIn');
        log_in_with(driver, data[0], data[1]);
        wait_for(driver, 'global-header-hamburger-button');
        return;

def log_into_Test(driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'headerSignIn'))
        )
    finally:
        with open("C:\LC\Testlogin.txt", "r") as text_file:
            data = text_file.readlines();
        click_on(driver, 'headerSignIn');
        log_in_with(driver, data[0], data[1]);
        wait_for(driver, 'global-header-hamburger-button');
        return;

def click_by_id(driver, id):
    print('A depretiated method has been used, Update to click_on');
    driver.find_element_by_id(id).click();
    time.sleep(1);
    return;

def click_on(driver, id):
    try:
        wait_for_page_to_clear(driver);
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, id)));
    finally:
        time.sleep(1)
        scroll_to_by_id(driver, id);
        wait_for(driver, id);
        driver.find_element(By.ID, id).click();
        return;

def click_by_css_selector(driver, css):
    try:
        wait_for_page_to_clear(driver);
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css)));

    finally:
        WebDriverWait(driver, 15).until_not(
            EC.presence_of_element_located((By.TAG_NAME, 'titan-form-overlay')));
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, css).click();
        time.sleep(0);
        return;

def click_by_name(driver, name):
    try:
        wait_for_page_to_clear(driver);
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, name)));

    finally:
        driver.find_element(By.NAME, name).click();
        time.sleep(1);
        return;

def click_by_xpath(driver, xpath):
    try:
        wait_for_page_to_clear(driver);
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, xpath)));

    finally:
        time.sleep(1)
        driver.find_element(By.XPATH, xpath).click();
        time.sleep(0);
        return;

def click_by_aria_label(driver, arialabel):
    try:
        wait_for_page_to_clear(driver);
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, xpath)));

    finally:
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "[aria-label='" + arialabel + "']").click();
        time.sleep(0);
        return;

def assert_by_id(driver, id):
    assert driver.find_element(By.ID, id);
    return;

def assert_by_text(driver, text):
    #assert driver.page_source.find(text);

    assert text in driver.page_source;
    return;

def should_see_text(driver, text):
    try:
        #wait_for_page_to_clear(driver);
        time.sleep(1);

    finally:
        source = driver.page_source;
        search_text = text;
        assert search_text in source;
        #print(search_text in source);
        return;

def should_not_see_text(driver, text):
    try:
        wait_for_page_to_clear(driver);
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, xpath)));

    finally:
        source = driver.page_source;
        search_text = text;
        assert search_text not in source;
        return;

def should_see_element(driver, id):
    try:
        wait_for_page_to_clear(driver);
        time.sleep(1);

    finally:
        driver.find_element(By.ID, id)
        return;

def text_is_displayed(driver, text):
    assert text in driver.page_source;
    print("This function is depcretated. Please use 'should_see_text'.")
    return;

def should_see_element(driver, id=None, class_name=None, tag_name=None, name=None, css_selector=None, xpath=None):
    try:
        wait_for_page_to_clear(driver);

    finally:
        if id==None:
            pass;
        else:
            driver.find_element(By.ID, id);
            return;

        if class_name==None:
            pass;
        else:
            driver.find_element(By.CLASS_NAME, class_name);
            return;

        if tag_name==None:
            pass;
        else:
            driver.find_element(By.TAG_NAME, tag_name);
            return;

        if name==None:
            pass;
        else:
            driver.find_element(By.NAME, name);
            return;

        if css_selector==None:
            pass;
        else:
            driver.find_element(By.CSS_SELECTOR, css_selector);
            return;

        if xpath==None:
            pass;
        else:
            driver.find_element(By.XPATH, xpath);
            return;
        return;

def button_is_disabled(driver, id):
    element = driver.find_element_by_id(id);
    if element.is_enabled():
        print("Test Failed")
        return;
    else:
        return;

def insert_text_by_id(driver, id, text):
    try:
        wait_for_page_to_clear(driver);
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, id)));

    finally:
        click_on(driver, id);
        actions = ActionChains(driver);
        actions.click(driver.find_element(By.ID, id));
        actions.double_click(driver.find_element(By.ID, id));
        actions.send_keys(Keys.DELETE);
        actions.send_keys(text);
        actions.perform();
        return;

def insert_text_by_aria_label(driver, arialabel, text):
    try:
        wait_for_page_to_clear(driver);
        #WebDriverWait(driver, 15).until(
        #    EC.presence_of_element_located((By.ID, id)));

    finally:
        click_by_aria_label(driver, arialabel);
        actions = ActionChains(driver);
        #driver.find_element(By.CSS_SELECTOR, "[aria-label='" + arialabel + "']").click();
        actions.click(driver.find_element(By.CSS_SELECTOR, "[aria-label='" + arialabel + "']"));
        actions.double_click(driver.find_element(By.CSS_SELECTOR, "[aria-label='" + arialabel + "']"));
        actions.send_keys(Keys.DELETE);
        actions.send_keys(text);
        actions.perform();
        return;

def insert_text_by_class(driver, class_name, text):
    try:
        wait_for_page_to_clear(driver);
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name)));

    finally:
        click_by_class_name(driver, class_name);
        driver.find_element_by_class_name(class_name).send_keys(Keys.DELETE);
        driver.find_element_by_class_name(class_name).clear();
        driver.find_element_by_class_name(class_name).send_keys(text);
        return;

def insert_text_by_css_selector(driver, css, text):
    try:
        wait_for_page_to_clear(driver);
    finally:
        click_by_css_selector(driver, css);
        actions = ActionChains(driver);
        actions.send_keys(Keys.DELETE);
        actions.send_keys(text);
        actions.perform();
        return;

def insert_text_by_xpath(driver, xpath, text):
    driver.find_element_by_xpath(xpath).clear();
    driver.find_element_by_xpath(xpath).send_keys(text);
    return;

def scroll_to_by_id(driver, id):
    wait_for(driver, id);
    element = driver.find_element(By.ID, id);
    element.location_once_scrolled_into_view;
    #driver.execute_script(
    #    "arguments[0].scrollIntoView({'block':'center','inline':'center'})",
    #    driver.find_element(By.ID, id)
    #);
    time.sleep(1);
    driver.execute_script("window.scrollBy(1000,-500);", "");
    #if element.is_displayed():
    #    pass;
    #else:
    #    time.sleep(3);
    #    element.location_once_scrolled_into_view;
    #    print('Please wait 3 seconds');
    #    print("scroll to element");
    #    print("scroll a little more");

    #driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, id));
    return;

def scroll_to_by_name(driver, name):
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_name(name));
    return;

def go_to_dashboard(driver):
    click_on(driver, 'global-header-hamburger-button');
    click_on(driver, 'Dashboard');
    return;

def go_to_account_page(self):
    click_on(self, 'global-header-hamburger-button');
    click_on(self, 'MealAccount');
    return;

def go_to_meal_application_page(driver, district):
    click_on(driver, 'global-header-hamburger-button');
    click_on(driver, 'MealApplication');
    click_on(driver, district);
    return;

def go_to_income_form(self):
    click_on(self, 'global-header-hamburger-button')
    click_on(self, 'IncomeForm')
    click_on(self, 'TITAN Unified School District')
    return;

def go_to_school_menu(self, school):
    click_on(self, 'global-header-hamburger-button')
    click_on(self, 'SchoolMenu')
    click_on(self, school)
    return;

def go_to_school_menu_as_guest(self):
    click_on(self, 'headerSchoolServices');
    click_on(self, 'headerSchoolServices-SchoolMenus');

def go_to_store(self, school):
    click_on(self, 'global-header-hamburger-button')
    click_on(self, 'Store')
    click_on(self, school)
    return;

def go_to_school_store_as_guest(self):
    click_on(self, 'headerSchoolServices');
    click_on(self, 'headerSchoolServices-SchoolStore');
    return;

def go_to_FAQ(self):
    click_on(self, 'headerFaq');
    return;

def go_to_forms(self):
    click_on(self, 'global-header-hamburger-button')
    click_on(self, 'Forms')
    return;

def go_to_history(self):
    click_on(self, 'global-header-hamburger-button')
    click_on(self, 'History')
    click_on(self, 'Purchase')
    return;

def go_to_profile(driver):
    click_on(driver, 'global-header-profile-button')
    click_on(driver, 'global-header-select-profile')
    return;

def open_shopping_cart(self):
    click_on(self, 'global-header-shopping-cart-button');
    time.sleep(1);
    assert_by_text(self, 'Cart');
    return;

def go_to_checkout(self):
    click_on(self, 'linqConnectSheetConfirmButton');
    return;

def confirm_and_pay(self):
    click_on(self, 'checkout-confirm-pay');
    return;

def go_to_district_dashboard(driver):
    click_on(driver, 'dashboard');
    return;

def remove_payment_reminder(self, id):
    click_on(self, id);
    return;

def wait_for(driver, id):
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, id))
        )
        #print('Done Waiting');
    finally:
        return;

def wait_for_page_to_clear(driver):
    WebDriverWait(driver, 5).until_not(
        EC.presence_of_element_located((By.TAG_NAME, 'titan-form-overlay')));
    WebDriverWait(driver, 15).until_not(
        EC.presence_of_element_located((By.CLASS_NAME, 'animating gray ispinner overlay')));
    WebDriverWait(driver, 5).until_not(
        EC.presence_of_element_located((By.CLASS_NAME, 'cdk-overlay-pane')));
    return;

def select_autopay_district(self, district_id):
    click_on(self, 'autoPayDistrictSelect');
    click_on(self, district_id);
    return;

def select_autopay_student(self, student_id):
    click_on(self, 'autoPayStudentSelection');
    click_on(self, student_id);
    return;

def click_by_class_name(driver, classname):
    driver.find_element(By.CLASS_NAME, classname).click();
    #driver.find_element_by_class_name(classname).click();
    return;

def wait_until_not_displayed(driver, name):
    try:
        WebDriverWait(driver, 60).until_not(
            EC.presence_of_element_located((By.CLASS_NAME, name)))
    finally:
        pass;
        return;

def deleteimage(location):
    try:
        os.remove('c:/testscreenshots/' + location);
    except OSError:
        pass;
    return

def take_screenshot(driver, location):
    try:
        # WebDriverWait(driver, 60).until_not(
        #     EC.presence_of_element_located((By.TAG_NAME, 'titan-form-overlay')));
        wait_for_page_to_clear(driver);
        time.sleep(2);
        #deleteimage(location);
        if os.path.exists('c:/testscreenshots/' + location): os.remove('c:/testscreenshots/' + location);
    finally:
        WebDriverWait(driver, 60).until_not(
            EC.presence_of_element_located((By.TAG_NAME, 'titan-form-overlay')));
        #time.sleep(2);

        driver.save_screenshot('c:/testscreenshots/' + location);
        return;

def refresh_the_page(driver):
    try:
        wait_for_page_to_clear(driver);
    finally:
        driver.refresh();
        WebDriverWait(driver, 15).until_not(
        EC.presence_of_element_located((By.CLASS_NAME, 'animating gray ispinner overlay')));
        time.sleep(2);
    return;

def switch_tab(driver, tab_number):
    driver.switch_to.window(driver.window_handles[tab_number]);
    return;

def log_into_district_portal(driver):
    driver.execute_script("window.open('');");
    driver.switch_to.window(driver.window_handles[1]);
    driver.get('https://staging.portal.titank12.com/login.html');
    insert_text_by_id(driver, 'userName', 'bburningham@linq.com');
    click_by_xpath(driver, '//*[@id="content-footer-container"]/div/div/div/div[3]/div/form/div[5]/button');
    insert_text_by_id(driver, 'password', 'Titan123!');
    click_by_xpath(driver, '/html/body/main/section/div/div/div/form/div[2]/button');
    return;

def log_into_test_district_portal(driver):
    driver.execute_script("window.open('');");
    driver.switch_to.window(driver.window_handles[1]);
    driver.get('https://test.portal.titank12.com/login.html');
    insert_text_by_id(driver, 'userName', 'bburningham@linq.com');
    click_by_xpath(driver, '//*[@id="content-footer-container"]/div/div/div/div[3]/div/form/div[5]/button');
    insert_text_by_id(driver, 'password', 'Titan123!');
    click_by_xpath(driver, '/html/body/main/section/div/div/div/form/div[3]/button');
    driver
    return;

def select_district(driver, district_id):
    click_on(driver, 'userName');
    click_on(driver, 'selectDistrict');
    insert_text_by_id(driver, 'searchTextx', district_id);
    click_on(driver, district_id);
    return;

def go_to_district_management(driver):
    click_on(driver, 'configuration');
    click_on(driver, 'configuration-district');
    click_on(driver, 'configuration-district-districtmanagement');
    return;

def change_district_timezone(driver, timezone):
    click_on(driver, 'timeZoneId');
    select = Select(driver.find_element(By.ID, 'timeZoneId'));
    select.select_by_value(timezone);
    click_on(driver, 'save');
    wait_for_page_to_clear(driver);
    return

def get_building_balance(driver, district_id, building_id):
    select_district(driver, district_id);
    click_on(driver, 'configuration');
    click_on(driver, 'configuration-buildings');
    click_on(driver, 'configuration-buildings-buildingmanagement');
    click_on(driver, building_id);
    wait_for(driver, 'configuration-buildings-buildingmanagement')
    return;

def set_language_to(driver, language):
    click_on(driver, 'languageSelector');
    click_on(driver, language);
    return;

def select_student(driver, studentID):
    click_on(driver, 'students');
    click_on(driver, 'students-studentmanagement');
    click_by_xpath(driver, '//*[@id="masterForm"]/titan-angular-root/ng-component/div/div[1]/accordion/accordion-group/div/div[1]/div/div');
    delement = Select(driver.find_element(By.ID, 'enrollmentStatus'));
    time.sleep(1)
    delement.select_by_visible_text('All');
    insert_text_by_id(driver, 'search', studentID);
    click_on(driver, studentID);
    return;

def update_student_info(driver, districtID, studentID, firstName=None, lastName=None, preferedName=None, birthDay=None):
    select_district(driver, districtID);
    select_student(driver, studentID);
    if lastName==None:
        pass;
    else:
        insert_text_by_id(driver, 'lastName', lastName);

    if firstName==None:
        pass;
    else:
        insert_text_by_id(driver, 'firstName', firstName);
    click_by_xpath(driver, '//*[@id="panel-general"]/div/div[3]/button[2]');
    #time.sleep(10);
    return;

def select_staff(driver, staffID):
    click_on(driver, 'staff');
    click_on(driver, 'staff-staffmanagement');
    insert_text_by_id(driver, 'search', staffID);
    click_on(driver, staffID);
    return;

def update_staff_info(driver, districtID, staffID, firstName=None, lastName=None, preferedName=None, birthDay=None):
    select_district(driver, districtID);
    select_staff(driver, staffID);
    if lastName==None:
        pass;
    else:
        insert_text_by_id(driver, 'lastName', lastName);

    if firstName==None:
        pass;
    else:
        insert_text_by_id(driver, 'firstName', firstName);
    click_on(driver, 'saveButton');
    #time.sleep(10);
    return;

def create_new_announcement(driver, districtID):
    select_district(driver, districtID);
    click_on(driver, 'utilities');
    click_on(driver, 'utilities-announcements');
    click_on(driver, 'add');
    insert_text_by_id(driver, 'name', 'Smoke Test ' + today());
    insert_text_by_id(driver, 'startDate', twodaysago());
    insert_text_by_id(driver, 'endDate', tomorrow());
    insert_text_by_css_selector(driver, '#text > div > div.fr-wrapper.show-placeholder', 'Test Me Automation')
    click_by_xpath(driver, '/html/body/modal-container/div/div/form/fieldset/div/div[4]/div[1]/div/label')
    click_by_xpath(driver, '/html/body/modal-container/div/div/form/fieldset/div/div[4]/div[2]/div/label')
    click_on(driver, 'save');
    #time.sleep(10);
    return;

def update_announcement(driver, districtID, endDate=None):
    select_district(driver, districtID);
    click_on(driver, 'utilities');
    click_on(driver, 'utilities-announcements');
    insert_text_by_id(driver, 'search', 'Smoke Test ' + today())
    click_on(driver, 'edit-0');
    insert_text_by_id(driver, 'endDate', endDate);
    click_on(driver, 'save');
    #time.sleep(10);
    return;

def add_new_autopay(driver, district=None, student=None, addAmount=None, belowAmount=None):
    scroll_to_by_id(driver, 'chevron-button-AutoPay');
    click_on(driver, 'addAutoPay');
    click_on(driver, 'autoPayDistrictSelect');
    click_on(driver, district);
    click_on(driver, 'autoPayStudentSelection');
    click_on(driver, student);
    click_by_class_name(driver, 'cdk-overlay-container');
    insert_text_by_id(driver, 'autoPaySlideOutAmountInput', addAmount);
    click_on(driver, 'autoPaySlideOutFrequencySelect')
    click_on(driver, 'autoPaySLideOutFrequencyOption-0')
    insert_text_by_id(driver, 'autoPaySlideOutFrequencyAmountInput', belowAmount);
    click_on(driver, 'linqConnectSheetConfirmButton');
    click_on(driver, 'dialog-confirm');
    wait_for_page_to_clear(driver);
    scroll_to_by_id(driver, 'chevron-button-AutoPay');
    return;

def link_staff(driver, districtName, staffId, firstName=None, lastName=None, DOB=None):
    #district = districtName
    district = "".join(districtName.split());
    click_on(driver, 'link-person-button-navbar');
    click_on(driver, 'personType');
    click_on(driver, 'Staff');
    insert_text_by_id(driver, 'districtSelect', districtName);
    time.sleep(2);
    click_on(driver, 'districtSelectorOption-'+ district);
    time.sleep(2);
    insert_text_by_id(driver, 'identifier', staffId);
    if firstName == None:
        pass;
    else:
        insert_text_by_id(driver, 'firstName', firstName);


    if lastName == None:
        pass;
    else:
        insert_text_by_id(driver, 'lastName', lastName);

    if DOB == None:
        pass;
    else:
        insert_text_by_id(driver, 'dateOfBirth', DOB);

    click_on(driver, 'linqConnectSheetConfirmButton');
    return;

def remove_linked_staff(driver, staff):
    click_on(driver, str(staff+'-personCardChevronButton-expandMore'));
    click_on(driver, str(staff+'-personCardKebab'));
    click_on(driver, 'null');
    return;

def go_to_LINQConnect_tab(driver):
    click_on(driver, 'districtmgt-familyPortal');
    return;

def enable_link_staff_by_DOB(driver):
    scroll_to_by_id(driver, 'isStaffDateOfBirthRequired');
    if driver.find_element(By.ID, 'isStaffDateOfBirthRequired').is_selected():
        return;
    else:
        click_on(driver, 'isStaffDateOfBirthRequired');
        click_on(driver, 'save');
    return;

def disable_link_staff_by_DOB(driver):
    scroll_to_by_id(driver, 'isStaffDateOfBirthRequired');
    if driver.find_element(By.ID, 'isStaffDateOfBirthRequired').is_selected():
        click_on(driver, 'isStaffDateOfBirthRequired');
        click_on(driver, 'save');
    else:
        return;
    return;

def log_out(driver):
    try:
        wait_for_page_to_clear(driver);
    finally:
        click_on(driver, 'global-header-profile-button');
        click_on(driver, 'global-header-logout');
        should_see_element(driver, id='landingPageLoginButton');
    return

def log_result(text):
    today = datetime.now();
    currentDate = today.strftime("%m-%d-%Y");
    resultfile = currentDate +'results.txt'
    testresult = open(resultfile, "a");
    testresult.write(text + '\n');
    testresult.close();
    return;
