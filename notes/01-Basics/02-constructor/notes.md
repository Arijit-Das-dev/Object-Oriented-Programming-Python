## Constructor
- Constructor is a function -> __init__(), which is executed when the class is being initialized.

- It has a fixed parameter called **self**.

- That **self** Parameter refers to the current object of the class when it is initialize.

### **Syntax :**
```python

class Student:

    def __init__(self):
        print("Devid is a student")
        print("Devid is a good student")

# self parameter refers by the help of __init__() function
# self parameter refers to that object
obj = Student()
```