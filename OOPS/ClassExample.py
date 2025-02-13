'''Classes in Object-Oriented Programming (OOP)
A class is a fundamental concept in Object-Oriented Programming (OOP). It acts as a blueprint for creating objects, 
which are instances of the class.A class defines attributes (data/variables) and methods (functions) that describe the
behavior of an object.
(or)
A class is a user-defined data type that groups variables (attributes) and functions (methods) into a single entity. 
It serves as a template from which multiple objects can be created.


2. Components of a Class

A class consists of:
Class Name – A meaningful identifier for the class.
Attributes (Instance Variables) – Data associated with the class.
Methods (Functions) – Define the behavior of the class.
Constructor – A special method to initialize objects when they are created.
Access Modifiers – Define the scope of class members (public, private, protected).


3. Characteristics of Classes
a) Attributes (Instance Variables)
Attributes represent state or characteristics of an object.
These variables store data specific to each object of the class.

b) Methods
Methods define behavior or actions that an object can perform.
They manipulate instance variables and perform operations.

c) Constructor (Initialization Method)
A constructor is a special method used for initializing an object when it is created.
In Python, the constructor method is __init__().

d) Access Modifiers
Public: Accessible from anywhere.
Private (__var): Not accessible outside the class.
Protected (_var): Accessible only within the class and its subclasses.

4. Types of Classes

Concrete Class:A regular class that can be instantiated into objects.
Abstract Class:A class that cannot be instantiated directly. It is meant to be inherited by other classes. 
It contains one or more abstract methods (methods without implementation).
Static Class:A class that only contains static methods and does not require object instantiation.
Singleton Class:A class that allows only one instance to exist.

'''

# 5. Advantages of Using Classes
# Encapsulation – Combines data and methods, restricting direct access.
# Code Reusability – Code can be reused by creating multiple objects of the same class.
# Scalability – Classes allow modular programming, making it easier to maintain.
# Data Abstraction – Hides implementation details and only exposes necessary functionalities.



class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display_info(self):
        return f"Car: {self.brand} {self.model}"
    
car1=Car("Toyota","camry")
car2=Car("Honda","civic")

print(car1.display_info())
print(car2.display_info())
        
    

# 2. Encapsulation (Private Attributes)

class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
    
    def deposit(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return f"Balance:{self.__balance}"
    
bank=BankAccount()
bank.deposit(200)
print(bank.get_balance())
# print(bank.__balance()) - get error

# 3. Inheritance (Parent-Child Relationship)


class Animal:
    def speak(self):
        return "Animal make sounds"
    
class Dog(Animal):
    def speak(self):
        return "bark"
    
class Cat(Animal):
    def speak(self):
        return "meow"
    
dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())

# 4. Polymorphism (Same Method, Different Behavior)

class Bird():
    def fly(self):
        return "Birds can fly"

class Penguin(Bird):
    def fly(self):
        return "Penguins can't fly"

bird=Bird()
penguin=Penguin()
print(bird.fly())
print(penguin.fly())


'''Access Specifiers in Classes (Python)
Access specifiers (also called access modifiers) in Object-Oriented Programming (OOP) define the visibility and 
accessibility of class members (attributes and methods). Python provides three access specifiers.

1. Public Access Specifier
Members declared as public can be accessed from anywhere (inside or outside the class).
By default, all class members in Python are public.



2. Protected Access Specifier (_protected)
Members declared as protected (prefix _ before the variable/method) can be accessed within the class and its subclasses.
It is not strictly private, 

3. Private Access Specifier (__private)
Members declared as private (prefix __ before variable/method) can only be accessed inside the class.
They cannot be accessed directly outside the class or by subclasses.

'''

class PublicClass:
    def show(self):
        return "I am a public class"

obj = PublicClass()
print(obj.show())  # ✅ Accessible anywhere



