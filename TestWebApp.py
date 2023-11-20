from lib2to3.pgen2 import driver
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Shared import dreamx_login_microsoft, dreamx_go_to_customize, dreamx_go_to_search, \
    dreamx_go_to_home, dreamx_go_to_dashboard, dreamx_go_to_story, dreamx_go_to_setting, \
    dreamx_customize, dreamx_logout, dreamx_go_to_contactInformation, dreamx_account_info, \
    dreamx_switch_to_teams, dreamx_switch_to_talent, dreamx_test_account, dreamx_go_to_account, \
    dreamx_switch_to_org, dreamx_manage_team, dreamx_manage_org\


@pytest.mark.usefixtures('chrome_driver')
class TestWebApp:
    def test_login_microsoft(self, chrome_driver, wait):
        dreamx_login_microsoft(chrome_driver, wait)
        try:
            chrome_driver.find_element(By.ID, 'item-home-0-Button')
        except NoSuchElementException:
            pytest.fail('Home button could not be found, login failed.', pytrace=False) 

    def test_customize(self, chrome_driver, wait):
        dreamx_login_microsoft(chrome_driver, wait)
        dreamx_go_to_setting(chrome_driver, wait)
        dreamx_customize(chrome_driver, wait)
        try:
            chrome_driver.find_element(By.ID, 'settings-bar-button-Customize')
        except NoSuchElementException:
            pytest.fail('Customize button could not be found, customization failed.', pytrace=False)
        dreamx_go_to_customize(chrome_driver, wait)


    def test_nav_bar(self, chrome_driver, wait):
        dreamx_login_microsoft(chrome_driver, wait)
        dreamx_go_to_search(chrome_driver, wait)
        dreamx_go_to_home(chrome_driver, wait)
        try:
            wait.until(EC.element_to_be_clickable((By.ID, 'item-home-0-Button')))
            chrome_driver.find_element(By.ID, 'item-home-0-Button')
        except NoSuchElementException:
            pytest.fail('Home button could not be found, Test failed.', pytrace=False)
        dreamx_go_to_dashboard(chrome_driver, wait)
        try:
            wait.until(EC.element_to_be_clickable((By.ID, 'item-dashboard-2-Button')))
            chrome_driver.find_element(By.ID, 'item-dashboard-2-Button')
        except NoSuchElementException:
            pytest.fail('Dashboard button could not be found, Test failed.', pytrace=False)
        dreamx_go_to_story(chrome_driver, wait)
        try:
            wait.until(EC.element_to_be_clickable((By.ID, 'item-story-3-Button')))
            chrome_driver.find_element(By.ID, 'item-story-3-Button')
        except NoSuchElementException:
            pytest.fail('Story button could not be found, Test failed.', pytrace=False)
        dreamx_go_to_setting(chrome_driver, wait)
        try:
            wait.until(EC.element_to_be_clickable((By.ID, 'CustomizeSectionTitle')))
            chrome_driver.find_element(By.ID, 'CustomizeSectionTitle')
        except NoSuchElementException:
            pytest.fail('Customize button could not be found, Test failed.', pytrace=False)
        dreamx_switch_to_teams(chrome_driver, wait)
        dreamx_switch_to_org(chrome_driver,wait)
        dreamx_switch_to_talent(chrome_driver,wait)
        dreamx_logout(chrome_driver, wait)

        
        

    def test_contact_info(self, chrome_driver, wait):
        dreamx_login_microsoft(chrome_driver, wait)
        dreamx_go_to_setting(chrome_driver, wait)
        dreamx_go_to_contactInformation(chrome_driver, wait)
        try:
            wait.until(EC.element_to_be_clickable((By.ID, 'ContactSectionTitle')))
            chrome_driver.find_element(By.ID, 'ContactSectionTitle')
        except NoSuchElementException:
            pytest.fail('Contact Information Title could not be found, Test failed.', pytrace=False)
        dreamx_account_info(chrome_driver, wait)


    def test_account(self, chrome_driver, wait):
            dreamx_login_microsoft(chrome_driver, wait)
            try:
                chrome_driver.find_element(By.ID, 'item-home-0-Button')
            except NoSuchElementException:
                pytest.fail('Home button could not be found, login failed.', pytrace=False) 
            dreamx_switch_to_teams(chrome_driver, wait)
            dreamx_go_to_setting(chrome_driver, wait)
            try:
                chrome_driver.find_element(By.ID, 'settings-bar-button-Account')
            except NoSuchElementException:
                pytest.fail('Account section could not be found, process failed.', pytrace=False) 
            dreamx_go_to_account(chrome_driver, wait)
            try:
                chrome_driver.find_element(By.ID, 'update-info-button')
            except NoSuchElementException:
                pytest.fail('Update Info button could not be found, process failed.', pytrace=False)
            dreamx_test_account(chrome_driver, wait)


    def test_manage_team(self, chrome_driver, wait):
        dreamx_login_microsoft(chrome_driver, wait)
        dreamx_switch_to_teams(chrome_driver, wait)
        dreamx_go_to_setting(chrome_driver, wait)
        try:
            chrome_driver.find_element(By.ID, 'settings-bar-button-Manage Members')
        except NoSuchElementException:
            pytest.fail('Manage members section could not be found, process failed.', pytrace=False) 
        dreamx_manage_team(chrome_driver, wait)
        try:
            chrome_driver.find_element(By.ID, 'settings-bar-button-Manage Members')
        except NoSuchElementException:
            pytest.fail('Manage members could not be found, process failed.', pytrace=False)

    def test_manage_org(self, chrome_driver, wait):
        dreamx_login_microsoft(chrome_driver, wait)
        dreamx_switch_to_org(chrome_driver, wait)
        dreamx_go_to_setting(chrome_driver, wait)
        try:
            chrome_driver.find_element(By.ID, 'settings-bar-button-Manage Members')
        except NoSuchElementException:
            pytest.fail('Manage members could not be found, process failed.', pytrace=False)         
        dreamx_manage_org(chrome_driver, wait)
        try:
            chrome_driver.find_element(By.ID, 'settings-bar-button-Manage Members')
        except NoSuchElementException:
            pytest.fail('Manage members could not be found, process failed.', pytrace=False)