import selenium
import pytest
#from behave import *
from pytest_bdd import scenarios, given, when, then, parsers
#from behave import  given, when, then
from selenium import webdriver

url = "http://automationpractice.com/index.php"


@scenarios("features/register.feature/")
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given('the home page is displayed')
def launch_web(browser):
    browser.get(url)


@when('user clicks on <sign in> button')
def sign_in_click(browser):
    sign_in_xpath = "//a[@class='login']"
    sign_in = browser.find_element_by_xpath(sign_in_xpath)
    sign_in.click()


@then("new page with <create an account> text is displayed")
def page_create_account(browser):
    create_acc_container_xpath = "//h3[contains(text(),'Create an account')]"
    create_acc_container = browser.find_element_by_xpath(create_acc_container_xpath)

    assert create_acc_container.text == "Create an account", print("test failed")
