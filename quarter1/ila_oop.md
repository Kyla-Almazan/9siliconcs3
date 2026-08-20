# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
    We keep all product details such as name, price, and stock, plus actions like updating stock inside one Product class. This data is kept safe and can only be changed through allowed methods instead of being modified directly anywhere in the program. This keeps everything organized and prevents accidental errors or wrong values. It makes the system easier to manage because all related information and actions stay in one place.

Code:
class Product:
    def __init_(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock
    def updated_stock(self, amount):
        self.__stock += amount

### 2. Abstraction
    We hide complicated details and only show simple features the user needs, such as adding a product or checking stock. The store owner does not need to know how the computer saves or calculates data. They only need to use the simple functions provided. This makes the system easy to use and less confusing. We can also improve the hidden parts later whithout breaking how the system works.

### 3. Inheritance
    We can create a main Product class and make special types of products from it, such as SpoilableProduct or PromoProduct. These child classes get all properties and actions from the main class and can add their own such as expiration date or dicount rate. We do not need to write the same code many times. This saves time, keeps code short, and makes adding new product types very easy.

Code:
class SpoilableProduct(Product):
    def __init__(self, name, price, stock, expiration_date):
        super().__init__(name, price, stock)
        self.expiration_date = expiration_date

### 4. Polymorphism
    This lets different product types use the same action name but behave in their own way. For example, a calculate_price method can work differently for regular items, discounted goods, or bulk products. All are called the same way but give the correct result for each type. This makes the system flexiblle and easy to expand. We can add new categories later without rewriting how we call these functions.

## Reflection
    Among the four pillars, Encapsulation is the most useful for the sari-sari store inventory system. It keeeps all product information and actions together in one place while protecting data from being changed incorrectly, which is very important for tracking prices and stock accurately. It makes the system organized, safe, and much easier to update or fix when needed. Without it, managing many products would get messy and cause errors easily.