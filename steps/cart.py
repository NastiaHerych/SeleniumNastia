import time
from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver


@given('open product = "{url}"')
def step(context, url):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://makeup.com.ua/ua/" + url)


@when('click buy button')
def step(context):
    context.driver.find_element(By.XPATH, "//div[contains(@class, 'product-item__button')]").click()
    time.sleep(3)


@when('check if in cart = "{product}"')
def step(context, product):
    xpath = f"//div[@class='product-list_product-item']//a[contains(@href, '{product}')]"
    context.driver.find_element(By.XPATH, xpath)
    time.sleep(3)

