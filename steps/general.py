from behave import *
from selenium import webdriver
import os


@given('open website')
def step(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://makeup.com.ua/ua/")


@given('a file with name "{filename}" exists in the project folder')
def create_file(context, filename):
    hello = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(hello + "\output", filename)
    with open(file_path, 'w'):
        pass

@then('the file should exist')
def check_file_existence(context, filename):
    assert filename, f"Filename not provided in the context"
    hello = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(hello + "\output", filename)
    assert os.path.exists(file_path), f"File report.html does not exist in the project folder"
