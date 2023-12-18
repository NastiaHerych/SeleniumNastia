from behave import *
import time
from selenium.webdriver.common.by import By


@when('change website language')
def step(context):
    assert context.driver.current_url == "https://makeup.com.ua/ua/"
    context.driver.find_element(By.XPATH, "//a[contains(@lang, 'ru')]").click()
    assert context.driver.current_url == "https://makeup.com.ua/"
    context.driver.quit()

