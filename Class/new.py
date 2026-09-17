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
        