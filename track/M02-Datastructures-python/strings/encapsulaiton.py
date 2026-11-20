# Encapsulation

class BankAcc:
    def __init__(self):
        self.__balance = 400  # private

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount


b = BankAcc()
print(b.get_balance())
b.set_balance(100)
print(b.get_balance())

# directly accessing private variable using name mangling
print(b._BankAcc__balance)


# Access Modifiers

# public - (name) -> accessible everywhere
class Student:
    def __init__(self):
        self.name = "John"

s = Student()
print(s.name)


# protected - (_name) -> accessible in same class and subclass
class Student:
    def __init__(self):
        self._name = "John"

class BioStudent(Student):
    def display(self):
        print(self._name)

s = Student()
bs = BioStudent()
print(s._name)
bs.display()


# private - (__name) -> accessible only in same class
class Student:
    def __init__(self):
        self.__name = "John"

s = Student()
print(s._Student__name)