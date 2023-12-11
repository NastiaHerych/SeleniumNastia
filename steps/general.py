from behave import *
from selenium import webdriver


@given('open website')
def step(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://makeup.com.ua/ua/")


