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


class MyTestCase(basetest.testFixture):
    @pytest.mark.testall
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

if __name__ == '__main__':
    unittest.main()
