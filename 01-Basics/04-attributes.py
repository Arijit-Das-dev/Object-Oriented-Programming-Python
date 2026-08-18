# Attributes
# There are two type of attributes
# 1. class attribute
# 2. object attribute
# object attr > class attribute


class Student:
    college = 'xyz' # class attribute

    def __init__(self, name, marks):

        self.name = name    # object attribute
        self.marks = marks

s1 = Student("Alex", 90)
print(s1.college)

print(s1.name)
print(s1.marks)