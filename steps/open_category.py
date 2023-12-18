from behave import *
import time
from selenium.webdriver.common.by import By


@when('open category = "{category}"')
def step(context, category):
    xpath = f"//a[contains(@href, '{category}')]"
    link = context.driver.find_element(By.XPATH, xpath)
    link.click()

