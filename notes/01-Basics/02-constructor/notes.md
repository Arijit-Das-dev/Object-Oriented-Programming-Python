## Constructor
- Constructor is a function -> __init__(), which is executed when the class is being initialized.

- It has a fixed parameter called **self**.

- That **self** Parameter refers to the current object of the class when it is initialize.

### Syntax :
```python

class Student:

    def __init__(self):
        print("Devid is a student")
        print("Devid is a good student")

# self parameter refers by the help of __init__() function
# self parameter refers to that object
obj = Student()
```


---
### Types of Constructor
- There are two types of constructors
- Type:
    - 1. Parameterized constructor - A constructor which takes parameters
        - [__init__(self, param1, param2)]

    - 2. Default constructor - A constructor which takes no parameters  
        - [__init__(self)]

### 1. Parameterized constructor
```python
class Student:

    # default constuctor
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(Self, param1, param2):
        pass
```