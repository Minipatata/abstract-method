#Write a program to create a base class that consists of two functions - 
# one to display a value, and another function is an abstract method. 
# Next, create a subclass that consists of a method similar to the abstract method. 
# Finally, showcase how Abstraction is being implemented in this example.
from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def debit(self):
        pass
    def credit(self):
        pass
class Desjardins(Bank):
    def debit(self):
        print("Money debited")
    def credit(self):
        print("Money credited")
m=Desjardins()
m.debit()
m.credit()