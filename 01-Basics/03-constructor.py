# Constructor -> __init__()
class Student:

    def __init__(self): # It is called a constructor
        print("Devid is a student")
        print("He is in 4th year")

# self parameter refers to that current object.
obj = Student()

# parameterized constuctor <- Takes multiple parameters
# __init__(self, param1, param2)

# default constructor <- Takes zero parameters except self
# __init__(self)