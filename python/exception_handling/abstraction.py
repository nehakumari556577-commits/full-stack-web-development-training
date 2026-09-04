from abc import ABC, abstractmethod

class Phone(ABC):

    @abstractmethod
    def power(self):
        pass

    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def display(self):
        pass

class SmartPhone(Phone):

    def power(self):
        print("Phone is turning ON")

    def call(self):
        print("Calling someone")

    def display(self):
        print("Displaying screen")

ob = SmartPhone()
ob.power()
ob.call()
ob.display()