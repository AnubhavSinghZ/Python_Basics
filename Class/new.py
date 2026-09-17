from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACTION
# ==========================================
# An abstract class acts as a blueprint. It hides complex 
# implementation details and enforces a structure on child classes.
class PaymentProcessor(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        """Abstract method: Must be implemented by all subclasses."""
        pass
# ==========================================
# 2. INHERITANCE
# ==========================================
# BankAccount is a base (parent) class. 
# It bundles properties and behaviors that other accounts will inherit.
class BankAccount(PaymentProcessor):
    # Class Attribute (shared by all instances)
    bank_name = "Apex Global Bank"
    
    # Constructor (__init__) - Initializes the object
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder  # Public attribute
        
        # ==========================================
        # 3. ENCAPSULATION
        # ==========================================
        # Using a double underscore (__) makes the attribute Private.
        # It cannot be accessed directly from outside the class.
        self.__balance = initial_balance 

    # Getter method to safely access private data
    def get_balance(self):
        return self.__balance

    # Setter method to safely modify private data with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

    # Implementing the abstract method from PaymentProcessor
    def process_payment(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Paid ${amount} via Bank Account. Remaining: ${self.__balance}")
        else:
            print("Insufficient funds for this payment.")


# SavingsAccount is a child class inheriting from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, interest_rate):
        # super() calls the parent class constructor to reuse its setup
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)
        print(f"Interest of ${interest} applied.")


# CreditCard is an independent class used to showcase Polymorphism
class CreditCard(PaymentProcessor):
    def __init__(self, card_holder, limit):
        self.card_holder = card_holder
        self.limit = limit 
# ==========================================
    # 4. POLYMORPHISM
    # ==========================================
    # Same method name ('process_payment') as BankAccount, but handles behavior differently.
    def process_payment(self, amount):
        if amount <= self.limit:
            self.limit -= amount
            print(f"Paid ${amount} using Credit Card. Remaining Limit: ${self.limit}")
        else:
            print("Credit limit exceeded!")


# ==========================================
# EXECUTION & DEMONSTRATION (Objects & Interaction)
# ==========================================
if __name__ == "__main__":
    print(f"--- Welcome to {BankAccount.bank_name} --- \n")

    # Creating Objects (Instantiation)
    savings = SavingsAccount("Alice", 1000, 2.5)
    credit_card = CreditCard("Bob", 5000)

    # 1. Testing Encapsulation
    print("--- 1. Testing Encapsulation ---")
    # print(savings.__balance) # <-- UNCOMMENTING THIS WILL RAISE AN ERROR (AttributeError)
    print(f"Account Holder: {savings.account_holder}")
    print(f"Initial Balance: ${savings.get_balance()}") # Accessed safely via getter
    savings.deposit(500) # Modified safely via setter
    print()

    # 2. Testing Inheritance
    print("--- 2. Testing Inheritance ---")
    savings.apply_interest() # Unique method inside the child class
    print()

    # 3. Testing Polymorphism & Abstraction
    print("--- 3. Testing Polymorphism & Abstraction ---")
    # We create a list of different objects that share the same abstract interface
    payment_methods = [savings, credit_card]

    # The loop triggers the exact same method name, but each object responds differently
    for method in payment_methods:
        method.process_payment(200)