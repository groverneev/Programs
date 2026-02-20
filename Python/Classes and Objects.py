"""
# How To Create A Class

# 1. Define the class name using the keyword CLASS
class Person():

    # 2. Initialize the class (Define the properties of the class)
    def __init__(self,name, age) -> None:
        self.name = name
        self.age = age
    
    # 3 Define the helper functions
    def printAge(self):
        print(self.age)

# 4. Create an object of the class
Neev = Person("Neev",12)
Neev.printAge()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

''' Library Management System '''

titles = ["The Great Gatsby", "To Kill a Mockingbird", "1984"]
authors = ["F. Scott Fitzgerald", "Harper Lee", "George Orwell"]
publication_dates = ["1925", "1960", "1949"]



class Book:
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date

    def __str__(self):
        return f"{self.title} by {self.author}, published {self.publication_date}"

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "1960")
book3 = Book("1984", "George Orwell", "1949")

print(book1)  # Output: The Great Gatsby by F. Scott Fitzgerald, published 1925

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

''' Question: Create a simple Bank Account Application '''
class BankingSystem:

    def __init__(self) -> None:
        self.balance = 0
    
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print("Your amount has been deopsited!")
        print("Your current balance is:", self.balance)
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            self.balance = self.balance - withdraw_amount
            print("Your amount has been subtracted!")
            print("Your current balance is:", self.balance)

        else:
            print("Please enter a number less than or equal to your current balance.")
    
    def checkBalance(self):
        print(self.balance)
person1 = BankingSystem()
person1.deposit(100)
person1.withdraw(99)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question: Create a Class for adding two complex numbers
class Adding_Numbers:
    def __init__(self, realnum1, imagnum1, realnum2, imagnum2):
        a = realnum1 + realnum2
        b = imagnum1 + imagnum2
        print(a, "+", b, end = "")
        print("i")
obj_1 = Adding_Numbers(3, 8, 2, 5)

#Create a Student class with attributes name, id, courses, and grades. Add methods add_course and add_grade that allow courses and grades to be added to the student's record. Add a method get_average_grade that returns the average grade for all of the student's courses.
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grade = []
        self.courses = []
    def add_course(self, course_name):
        self.courses.append(course_name)
        self.grade.append(None)
    def add_grade(self, course_name, course_grade):
        a = self.courses.index(course_name)
        self.grade[a] = course_grade
    def avg_grade(self):
        a = 0
        for b in range(len(self.grade)):
            a = a + self.grade[b]
        print(a/len(self.grade))
student_1 = Student("Bob", 1241234563)
student_1.add_course("Math")
student_1.add_course("Science")
student_1.add_course("P.E.")
student_1.add_course("English")
student_1.add_grade("Math", 89)
student_1.add_grade("Science", 100)
student_1.add_grade("P.E.", 10)
student_1.add_grade("English", 46)
student_1.avg_grade()
"""

#Create a ShoppingCart class that allows users to add and remove items from a shopping cart. Add methods to calculate the total cost of the items in the cart, and to check out and complete the purchase.
import sys
class ShoppingCart():
    def __init__(self, username):
        self.username = username
        self.cart_items = []
        self.cart_price = []
        self.cart_qty = []
    def add_item(self, item_name, item_price, item_qty):
        self.cart_items.append(item_name)
        self.cart_price.append(item_price)
        self.cart_qty.append(item_qty)
    def remove_item(self, item_name):
        a = self.cart_items.index(item_name)
        self.cart_items.remove(a)
        self.cart_price.remove(a)
        self.cart_qty.remove(a)
    def total_cost(self):
        cost = 0
        for z in range(len(self.cart_items)):
            cost = cost + (self.cart_price[z] * self.cart_qty[z])
        return cost
    def checkout(self):
        print("Your total cost is", self.total_cost(), "dollars. Would you like to check out? (y/n)")
        a = input()
        if a == "y":
            print("You have successfully checked out!")
            sys.exit()
person1 = ShoppingCart("Bob")
person1.add_item("Broccoli", 13, 24)
person1.checkout()