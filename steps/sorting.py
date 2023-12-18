from behave import *
import time
from selenium.webdriver.common.by import By


@when('sort by price = "{price}"')
def step(context, price):
    xpath = f"//li[contains(@id, '{price}')]"
    link = context.driver.find_element(By.XPATH, xpath)
    link.click()

