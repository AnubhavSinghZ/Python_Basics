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
