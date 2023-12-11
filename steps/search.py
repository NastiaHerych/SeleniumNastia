from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


@when('open search form')
def step(context):
    context.driver.find_element(By.XPATH, "//div[contains(@class, 'search-button')]").click()


@when('input search = "{search}"')
def step(context, search):
    context.driver.find_element(By.NAME, "q").send_keys(search)
    wait = WebDriverWait(context.driver, 3)
    wait.until(EC.visibility_of_element_located((By.NAME, 'q')))


@when('run search')
def step(context):
    context.driver.find_element(By.XPATH, "//form//button[contains(@class, 'search-button')]").click()
    time.sleep(3)
    context.driver.quit()
