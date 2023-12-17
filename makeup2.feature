Feature:
#  4.	Зміна мови на сайті.
  Scenario: Change language
    Given open website
    When change website language

#5.	Додавання товару до кошика та перевірка наявності цього товару в кошику.
  Scenario: Add item to cart
    Given open product = "/product/127021/"
    When click buy button
    When check if in cart = "/product/127021/"