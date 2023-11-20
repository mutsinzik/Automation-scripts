import os
import boto3
import boto3.session
import pytest
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

@pytest.fixture()
def devicefarm_client():
    load_dotenv()
    ENV = os.environ['ENV']

    if ENV == 'dev':
        return boto3.session.Session(profile_name='dev').client('devicefarm', region_name='us-west-2')
    else:
        return boto3.client('devicefarm', region_name='us-west-2')

@pytest.fixture()
def chrome_driver(devicefarm_client):
    load_dotenv()
    testgrid_url_response = devicefarm_client.create_test_grid_url(
        projectArn=os.environ['DEVICE_FARM_PROJECT_ARN'],
        expiresInSeconds=500)
    driver = Remote(testgrid_url_response['url'], DesiredCapabilities.CHROME)
    yield driver
    driver.close()
    driver.quit()

@pytest.fixture()
def wait(chrome_driver):
    wait = WebDriverWait(chrome_driver, 20)
    return wait
