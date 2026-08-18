# Methods
# Methods are the functions or the features that belong to the class and their objects.

class Person:

    def __init__(self, full_name):
        self.full_name = full_name

    def greet(self):
        return f"Hello {self.full_name}"

p = Person("Devid")
print(p.greet())