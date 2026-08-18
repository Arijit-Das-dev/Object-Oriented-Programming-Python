## Attributes
- Attributes are the collection of qualities of a class or an object
- Attributes are two types :
    - class attribute
    - object attribute

### Syntax :
```python

class Student:
    college = 'xyz' # class attribute

    def __init__(self, name, marks):

        self.name = name    # object attribute
        self.marks = marks

s1 = Student("Alex", 90)
print(s1.college)

print(s1.name)
print(s1.marks)
```