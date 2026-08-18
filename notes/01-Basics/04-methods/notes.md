## Methods
- Methods are the features or the functionalities which is belong to the class and it's objects.

## Syntax :
```python

class Person:

    def __init__(self, full_name):
        self.full_name = full_name

    def greet(self):
        return f"Hello {self.full_name}"

p = Person("Devid")
print(p.greet())
```