import os
import time
from dotenv import load_dotenv
from lib2to3.pgen2.driver import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


# Login with microsoft
def dreamx_login_microsoft(driver, wait):
    load_dotenv()
    driver.maximize_window()
    driver.get(os.environ['STAGE_URL'])
    # Select agree to the terms
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.ID, 'checkbox-terms-privacy')))
    driver.find_element(By.ID, 'checkbox-terms-privacy').click()
    # Click on Microsoft icon
    wait.until(EC.element_to_be_clickable((By.ID, 'social-button-icon-1')))
    driver.find_element(By.ID, 'social-button-icon-1').click()
    # Enter username
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.ID, 'i0116')))
    driver.find_element(By.ID, 'i0116').send_keys(os.environ['TALENT_USERNAME'])
    driver.find_element(By.ID, 'idSIButton9').click()
    # Enter password
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.ID, 'i0118')))
    driver.find_element(By.ID, 'i0118').send_keys(os.environ['MICROSOFT_PASSWORD'])
    driver.find_element(By.ID, 'idSIButton9').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'idBtn_Back')))
    driver.find_element(By.ID, 'idBtn_Back').click()
    # Select a Plan
    # wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/section/div/div/div/form/div[3]/button[1]')))
    # driver.find_element(By.XPATH, '/html/body/div[1]/main/section/div/div/div/form/div[3]/button[1]').click()
    try:
        driver.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/form/div[3]/button[1]')
        driver.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/form/div[3]/button[1]').click()
    except NoSuchElementException:
        print('Element not found')

# Login with Google Account

def dreamx_login_Google(driver, wait):
    load_dotenv()
    driver.maximize_window()
    driver.get(os.environ['STAGE_URL'])
    # Select agree to the terme and chose microsoft
    wait.until(EC.element_to_be_clickable((By.ID, 'checkbox-terms-privacy')))
    driver.find_element(By.ID, 'checkbox-terms-privacy').click()
    # Click on the Google Icon
    wait.until(EC.element_to_be_clickable((By.ID, 'social-button-icon-2')))
    driver.find_element(By.ID, 'social-button-icon-2').click()
    # Enter Username 
    wait.until(EC.element_to_be_clickable((By.ID, 'identifierId')))
    driver.find_element(By.ID, 'identifierId').send_keys(os.environ['GMAIL_EMAIL'])
    driver.find_element(By.ID, 'identifierNext').click()
    # Enter Password
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')))
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(os.environ['GMAIL_PASSWORD'])
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    # Pass the Security process
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/button')))
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/button').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/button')))
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/button').click()
    # Select a Plan
    wait.until(EC.element_to_be_clickable((By.XPATH, 'talentPlanActivateButton')))
    driver.find_element(By.XPATH, 'talentPlanActivateButton').click()
  

# Logout from DreamX
def dreamx_logout(driver, wait):
    wait.until(EC.element_to_be_clickable((By.ID, 'item-profile-0-Button')))
    driver.find_element(By.ID, 'item-profile-0-Button').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'logoutButton')))
    driver.find_element(By.ID, 'logoutButton').click()


# Go to setting section
def dreamx_go_to_setting(driver, wait):
    wait.until(EC.element_to_be_clickable((By.ID, 'item-profile-0-Button')))
    driver.find_element(By.ID, 'item-profile-0-Button').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'settingButton')))
    driver.find_element(By.ID, 'settingButton').click()


# Go to Contact Information when you are in the setting section
def dreamx_go_to_contactInformation(driver, wait):
    wait.until(EC.element_to_be_clickable((By.ID, 'settings-bar-button-Contact Information')))
    driver.find_element(By.ID, 'settings-bar-button-Contact Information').click()


# Go to Customize when you are in the setting section
def dreamx_go_to_customize(driver, wait):
    wait.until(EC.element_to_be_clickable((By.ID, 'settings-bar-button-Customize')))
    driver.find_element(By.ID, 'settings-bar-button-Customize').click()


# Go to Plan when you are in the setting section
def dreamx_go_to_plan(driver, wait):
    wait.until(EC.element_to_be_clickable((By.ID, 'planButtonSection')))
    driver.find_element(By.ID, 'planButtonSection').click()


# Go to Account when you are in the setting section
def dreamx_go_to_account(driver, wait):
    wait.until(EC.element_to_be_clickable((By.ID, 'settings-bar-button-Account')))
    driver.find_element(By.ID, 'settings-bar-button-Account').click()


# Go to Application when you are in the setting section
def dreamx_go_to_applications(driver, wait):
    wait.until(EC.element_to_be_clickable((By.ID, 'applicationsButtonSection')))
    driver.find_element(By.ID, 'applicationsButtonSection').click()


# Go to Home 
def dreamx_go_to_home(driver, wait):
    wait.until(EC.element_to_be_clickable((By.ID, 'item-home-0-Button')))
    driver.find_element(By.ID, 'item-home-0-Button').click()


# Go to Search
def dreamx_go_to_search(driver, wait):
    wait.until(EC.element_to_be_clickable((By.ID, 'item-search-1-Button')))
    driver.find_element(By.ID, 'item-search-1-Button').click()


# Go to Dashboard
def dreamx_go_to_dashboard(driver, wait):
    wait.until(EC.element_to_be_clickable((By.ID, 'item-dashboard-2-Button')))
    driver.find_element(By.ID, 'item-dashboard-2-Button').click()


# Go to Story
def dreamx_go_to_story(driver, wait):
    wait.until(EC.element_to_be_clickable((By.ID, 'item-story-3-Button')))
    driver.find_element(By.ID, 'item-story-3-Button').click()


# Enter information in Account Customization section
def dreamx_customize(driver, wait):
    # Select Interface Language as English
    wait.until(EC.element_to_be_clickable((By.ID, 'interfaceLanguageSelect')))
    driver.find_element(By.ID, 'interfaceLanguageSelect').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'English (Canada)')))
    driver.find_element(By.ID, 'English (Canada)').click()
    # Change the app's theme
    # wait.until(EC.element_to_be_clickable((By.ID, 'themeSelect')))
    # driver.find_element(By.ID, 'themeSelect').click()
    # wait.until(EC.element_to_be_clickable((By.ID, 'default')))
    # driver.find_element(By.ID, 'default').click()


# Click on the nav bar Create (+) button
def dreamx_create_button(driver, wait):
    wait.until(EC.element_to_be_clickable((By.ID, 'sideNavCreateButtonIcon')))
    driver.find_element(By.ID, 'sideNavCreateButtonIcon').click()


# Enter information in Account Information
def dreamx_account_info(driver, wait):
    # Add another email in Contact information
    wait.until(EC.element_to_be_clickable((By.ID, 'email-contact-information-add-another-button')))
    driver.find_element(By.ID, 'email-contact-information-add-another-button').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'email-validation-text-field')))
    driver.find_element(By.ID, 'email-validation-text-field').send_keys('test.user@gmail.com')
    wait.until(EC.element_to_be_clickable((By.ID, 'email-contact-information-verify-button')))
    driver.find_element(By.ID, 'email-contact-information-verify-button').click()
    # Add another phone number in Contact Information
    wait.until(EC.element_to_be_clickable((By.ID, 'phone-contact-information-add-another-button')))
    driver.find_element(By.ID, 'phone-contact-information-add-another-button').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'phone-text-field')))
    driver.find_element(By.ID, 'phone-text-field').send_keys('613-555-0107')
    wait.until(EC.element_to_be_clickable((By.ID, 'phone-contact-information-verify-button')))
    driver.find_element(By.ID, 'phone-contact-information-verify-button').click()
    # Add Personal Website
    wait.until(EC.element_to_be_clickable((By.ID, 'website-contact-information-add-another-button')))
    driver.find_element(By.ID, 'website-contact-information-add-another-button').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'website-validation-text-field')))
    driver.find_element(By.ID, 'website-validation-text-field').send_keys('test.com')
    wait.until(EC.element_to_be_clickable((By.ID, 'website-contact-information-verify-button')))
    driver.find_element(By.ID, 'website-contact-information-verify-button').click()
    # Delete email
    wait.until(EC.element_to_be_clickable((By.ID, 'email-contact-information-delete-icon-1')))
    driver.find_element(By.ID, 'email-contact-information-delete-icon-1').click()
    # Delete Phone number
    wait.until(EC.element_to_be_clickable((By.ID, 'phone-contact-information-delete-icon-1')))
    driver.find_element(By.ID, 'phone-contact-information-delete-icon-1').click()
    # Delete custom website
    wait.until(EC.element_to_be_clickable((By.ID, 'website-contact-information-delete-icon-1')))
    driver.find_element(By.ID, 'website-contact-information-delete-icon-1').click()

def dreamx_switch_to_teams(driver, wait):
    # Switch Teams
    wait.until(EC.element_to_be_clickable((By.ID, 'item-profile-0-Button')))
    driver.find_element(By.ID, 'item-profile-0-Button').click()
    wait.until(EC.element_to_be_clickable((By.ID,'switchToTeamButton')))
    driver.find_element(By.ID,'switchToTeamButton').click()
    wait.until(EC.element_to_be_clickable((By.ID,'menuItema3630d5f-cd62-442b-aed5-9b3c8255faac')))
    driver.find_element(By.ID,'menuItema3630d5f-cd62-442b-aed5-9b3c8255faac').click()


def dreamx_switch_to_org(driver, wait):

    wait.until(EC.element_to_be_clickable((By.ID, 'item-profile-0-Button')))
    driver.find_element(By.ID, 'item-profile-0-Button').click()
    wait.until(EC.element_to_be_clickable((By.ID,'switchToOrganizationButton')))
    driver.find_element(By.ID,'switchToOrganizationButton').click()


def dreamx_switch_to_talent(driver, wait):

    wait.until(EC.element_to_be_clickable((By.ID, 'item-profile-0-Button')))
    driver.find_element(By.ID, 'item-profile-0-Button').click()
    wait.until(EC.element_to_be_clickable((By.ID,'switchToTalentButton')))
    driver.find_element(By.ID,'switchToTalentButton').click()

def dreamx_test_account(driver, wait):
        # Update Payment Info
        wait.until(EC.element_to_be_clickable((By.ID, 'update-info-button')))
        driver.find_element(By.ID, 'update-info-button').click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/span/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/a/div/div[2]')))
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/span/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/a/div/div[2]').click()
        driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/span/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/iframe'))
        wait.until(EC.element_to_be_clickable((By.ID, 'Field-numberInput')))
        driver.find_element(By.ID, 'Field-numberInput').click()
        driver.find_element(By.ID, 'Field-numberInput').send_keys(os.environ['Stripe'])
        wait.until(EC.element_to_be_clickable((By.ID, 'Field-expiryInput')))
        driver.find_element(By.ID, 'Field-expiryInput').click()
        driver.find_element(By.ID, 'Field-expiryInput').send_keys('1124')
        wait.until(EC.element_to_be_clickable((By.ID, 'Field-cvcInput')))
        driver.find_element(By.ID, 'Field-cvcInput').click()
        driver.find_element(By.ID, 'Field-cvcInput').send_keys('321')
        wait.until(EC.element_to_be_clickable((By.ID, 'Field-postalCodeInput')))
        driver.find_element(By.ID, 'Field-postalCodeInput').click()
        driver.find_element(By.ID, 'Field-postalCodeInput').send_keys('90210')
        driver.switch_to.default_content()
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/span/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/button/div')))
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/span/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/button/div').click()
    
        # Delete Payment Info
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/span/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/button/div')))
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/span/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/button/div').click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div/span/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/button')))
        driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/span/div/div/div/div/div[3]/div/div/div/div[2]/div/div[1]/button').click()        

        # Return To Account section
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/span/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div/div/div[2]/a')))
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/span/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div/div/div[2]/a').click()

        # Change Team Status
        wait.until(EC.element_to_be_clickable((By.ID, 'interfaceLanguageSelect')))
        driver.find_element(By.ID, 'interfaceLanguageSelect').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'inactive')))
        driver.find_element(By.ID, 'inactive').click()


# Manage a Team
def dreamx_manage_team(driver, wait):
    # Go to Manage members
        wait.until(EC.element_to_be_clickable((By.ID, 'settings-bar-button-Manage Members')))
        driver.find_element(By.ID, 'settings-bar-button-Manage Members').click()
    # Change a Member to admin
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-2717b51f-2e65-4170-826d-97b8870fa8ae')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-2717b51f-2e65-4170-826d-97b8870fa8ae').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-1')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-1').click()

    # Change status to Collaborator
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-2717b51f-2e65-4170-826d-97b8870fa8ae')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-2717b51f-2e65-4170-826d-97b8870fa8ae').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-3')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-3').click()

    # Change a Member to Owner

        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-2717b51f-2e65-4170-826d-97b8870fa8ae')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-2717b51f-2e65-4170-826d-97b8870fa8ae').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-0')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-0').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'confirmDialogConfirmButton')))
        driver.find_element(By.ID, 'confirmDialogConfirmButton').click()     

    # Change a member's status
        # Inactive
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-status-select-2')))
        driver.find_element(By.ID, 'team-org-management-table-status-select-2').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'statusMenuItemInactive')))
        driver.find_element(By.ID, 'statusMenuItemInactive').click()        
        # Active
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-status-select-0')))
        driver.find_element(By.ID, 'team-org-management-table-status-select-0').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'statusMenuItemActive')))
        driver.find_element(By.ID, 'statusMenuItemActive').click()   

        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-f3026daf-c489-44b5-8986-bdf5e00d639f')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-f3026daf-c489-44b5-8986-bdf5e00d639f').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-0')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-0').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'confirmDialogConfirmButton')))
        driver.find_element(By.ID, 'confirmDialogConfirmButton').click()
    
 
    # Search members in a team
        wait.until(EC.element_to_be_clickable((By.ID, 'teamOrgManagementSearchField')))
        driver.find_element(By.ID, 'teamOrgManagementSearchField').click()
        driver.find_element(By.ID, 'teamOrgManagementSearchField').send_keys('Kabuto')
        driver.find_element(By.ID, 'teamOrgManagementSearchField').send_keys(Keys.CONTROL, 'a')
        driver.find_element(By.ID, 'teamOrgManagementSearchField').send_keys(Keys.BACKSPACE)

    
    # Delete a Member in a team
        wait.until(EC.element_to_be_clickable((By.ID, 'mini-button-delete-1')))
        driver.find_element(By.ID, 'mini-button-delete-1').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'confirmDialogConfirmButton')))
        driver.find_element(By.ID, 'confirmDialogConfirmButton').click()

    # Add a member in a team
        wait.until(EC.element_to_be_clickable((By.ID, 'inviteMembersButton')))
        driver.find_element(By.ID, 'inviteMembersButton').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'email-validation-text-field')))
        driver.find_element(By.ID, 'email-validation-text-field').click()
        driver.find_element(By.ID, 'email-validation-text-field').send_keys('dev.test@gmail.com')
        wait.until(EC.element_to_be_clickable((By.ID, 'inviteButton')))
        driver.find_element(By.ID, 'inviteButton').click()


# Manage an Org:
def dreamx_manage_org(driver, wait):
        # Go to Manage members
        wait.until(EC.element_to_be_clickable((By.ID, 'settings-bar-button-Manage Members')))
        driver.find_element(By.ID, 'settings-bar-button-Manage Members').click()

    # Change a Member to admin
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-6c1766db-6bf1-4559-a237-9f656137abef')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-6c1766db-6bf1-4559-a237-9f656137abef').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-1')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-1').click()

    # Change status to Collaborator
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-6c1766db-6bf1-4559-a237-9f656137abef')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-6c1766db-6bf1-4559-a237-9f656137abef').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-3')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-3').click()

    # Change a Member to Owner

        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-6c1766db-6bf1-4559-a237-9f656137abef')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-6c1766db-6bf1-4559-a237-9f656137abef').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-0')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-0').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'confirmDialogConfirmButton')))
        driver.find_element(By.ID, 'confirmDialogConfirmButton').click()   

    # Change a member's status
        # Inactive
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-status-select-0')))
        driver.find_element(By.ID, 'team-org-management-table-status-select-0').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'statusMenuItemInactive')))
        driver.find_element(By.ID, 'statusMenuItemInactive').click()        
        # Active
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-status-select-0')))
        driver.find_element(By.ID, 'team-org-management-table-status-select-0').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'statusMenuItemActive')))
        driver.find_element(By.ID, 'statusMenuItemActive').click()     

        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-8831bdde-213e-4bbb-959b-332fcbb63ac9')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-8831bdde-213e-4bbb-959b-332fcbb63ac9').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'team-org-management-table-member-type-select-0')))
        driver.find_element(By.ID, 'team-org-management-table-member-type-select-0').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'confirmDialogConfirmButton')))
        driver.find_element(By.ID, 'confirmDialogConfirmButton').click()

    # Search members in a team
        wait.until(EC.element_to_be_clickable((By.ID, 'teamOrgManagementSearchField')))
        driver.find_element(By.ID, 'teamOrgManagementSearchField').click()
        driver.find_element(By.ID, 'teamOrgManagementSearchField').send_keys('Kabuto')
        driver.find_element(By.ID, 'teamOrgManagementSearchField').send_keys(Keys.CONTROL, 'a')
        driver.find_element(By.ID, 'teamOrgManagementSearchField').send_keys(Keys.BACKSPACE)

    # Delete a Member in a team
        wait.until(EC.element_to_be_clickable((By.ID, 'mini-button-delete-2')))
        driver.find_element(By.ID, 'mini-button-delete-2').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'confirmDialogConfirmButton')))
        driver.find_element(By.ID, 'confirmDialogConfirmButton').click()

    # Add a member in a team
        wait.until(EC.element_to_be_clickable((By.ID, 'inviteMembersButton')))
        driver.find_element(By.ID, 'inviteMembersButton').click()
        wait.until(EC.element_to_be_clickable((By.ID, 'email-validation-text-field')))
        driver.find_element(By.ID, 'email-validation-text-field').click()
        driver.find_element(By.ID, 'email-validation-text-field').send_keys('dev.test@gmail.com')
        wait.until(EC.element_to_be_clickable((By.ID, 'inviteButton')))
        driver.find_element(By.ID, 'inviteButton').click()