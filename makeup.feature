# behave .\features\makeup.feature
Feature:

#  1.	Пошук товару на сайті за заданим запитом.
#  Scenario: Search item
    Given open website
    When open search form
    When input search = "Calvin Klein"
    And run search

#  2.	Сортування товарів за ціною.
  Scenario: Sort by price
    Given open website
    When open category = "/ua/categorys/20273/"
    When sort by price = "catalog-price-dia-_2"

#  3.	Перехід з головної сторінки до категорії товарів.
  Scenario: Open category
    Given open website
    When open category = "/ua/categorys/20272/"
    When open category = "/ua/categorys/20280/"



  @last_scenario
  Scenario: Verify report existence
    Given a file with name "report.html" exists in the project folder
    Then the file should exist "report.html"
